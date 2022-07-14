from abc import ABC, abstractmethod
from collections import namedtuple
from dataclasses import dataclass, field
from datetime import date
from os import getenv
from pathlib import Path
from typing import Any, List, Optional, NamedTuple
from urllib.request import urlretrieve
import logging

from bs4 import BeautifulSoup as Soup  # type: ignore
logging.basicConfig(level=logging.DEBUG)

TMP = getenv("TMP", "/tmp")
TODAY = date.today()
# Candidate = namedtuple("Candidate", "name votes")


class Candidate(NamedTuple):
    name: str
    votes: int
# LeaderBoard = namedtuple(
#     "LeaderBoard", "Candidate Average Delegates Contributions Coverage"
# )


class LeaderBoard(NamedTuple):
    Candidate: str
    Average: float
    Delegates: str
    Contributions: str
    Coverage: int
# Poll = namedtuple(
#     "Poll",
#     "Poll Date Sample Sanders Biden Gabbard Spread",
# )


class Poll(NamedTuple):
    Date: str
    Sample: str
    Sanders: float
    Biden: float
    Gabbard: float
    Spread: str


@dataclass
class File:
    """File represents a filesystem path.

    Variables:
        name: str -- The filename that will be created on the filesystem.
        path: Path -- Path object created from the name passed in.

    Methods:
        [property]
        data: -> Optional[str] -- If the file exists, it returns its contents.
            If it does not exist, it returns None.
    """
    name: str
    path: Path = field(init=False)

    @property
    def data(self) -> Optional[str]:
        if self.path.is_file():
            return self.path.read_text()
        return None

    def __post_init__(self):
        self.path = Path(TMP).joinpath(f"{TODAY}_{self.name}")


@dataclass
class Web:
    """Web object.

    Web is an object that downloads the page from the url that is passed
    to it and stores it in the File instance that is passed to it. If the
    File already exists, it just reads the file, otherwise it downloads it
    and stores it in File.

    Variables:
        url: str -- The url of the web page.
        file: File -- The File object to store the page data into.

    Methods:
        [property]
        data: -> Optional[str] -- Reads the text from File or retrieves it from the
            web if it does not exists.

        [property]
        soup: -> Soup -- Parses the data from File and turns it into a BeautifulSoup
            object.
    """
    url: str
    file: File

    @property
    def data(self) -> Optional[str]:
        """Reads the data from the File object.

        First it checks if the File object has any data. If it doesn't, it retrieves
        it and saves it to the File. It then reads it from the File and returns it.

        Returns:
            Optional[str] -- The string data from the File object.
        """
        if self.file.data is None:
            urlretrieve(self.url, self.file.path)
        return self.file.data

    @property
    def soup(self) -> Soup:
        """Converts string data from File into a BeautifulSoup object.

        Returns:
            Soup -- BeautifulSoup object created from the File.
        """
        return Soup(self.data, 'html.parser')


@dataclass
class Site(ABC):
    """Site Abstract Base Class.

    Defines the structure for the objects based on this class and defines the interfaces
    that should be implemented in order to work properly.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        [abstractmethod]
        parse_rows: -> Union[List[LeaderBoard], List[Poll]] -- Parses a BeautifulSoup
            table element and returns the text found in the td elements as
            namedtuples.

        [abstractmethod]
        polls: -> Union[List[LeaderBoard], List[Poll]] -- Does the parsing of the table
            and rows for you. It takes the table index number if given, otherwise
            parses table 0.

        [abstractmethod]
        stats: -- Formats the results from polls into a more user friendly
            representation.
    """
    web: Web

    @staticmethod
    def _str_to_int(x):
        try:
            return int(x)
        except:
            return 0

    @staticmethod
    def _str_to_float(x):
        try:
            return float(x)
        except:
            return 0

    def find_table(self, loc: int = 0) -> str:
        """Finds the table elements from the Soup object

        Keyword Arguments:
            loc {int} -- Parses the Web object for table elements and
                returns the first one that it finds unless an integer representing
                the required table is passed. (default: {0})

        Returns:
            str -- The html table
        """
        return (tables := self.web.soup.findAll("table")[loc])

    @abstractmethod
    def parse_rows(self, table: Soup) -> List[Any]:
        """Abstract Method

        Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as NamedTuple.

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        pass

    @abstractmethod
    def polls(self, table: int = 0) -> List[Any]:
        """Abstract Method

        Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[NamedTuple] -- List of NamedTuple that were created from the
                table data.
        """
        table_soup = self.find_table(table)
        return self.parse_rows(table_soup)

    @abstractmethod
    def stats(self, loc: int = 0):
        """Abstract Method

        Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        pass


@dataclass
class RealClearPolitics(Site):
    """RealClearPolitics object.

    RealClearPolitics is a custom class to parse a Web instance from the
    realclearpolitics website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[Poll] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as Poll namedtuples.

        polls: -> List[Poll] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            RealClearPolitics
            =================
                Biden: 214.0
              Sanders: 142.0
              Gabbard: 6.0

    """

    def parse_rows(self, table: Soup) -> List[Poll]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as Poll namedtuples.

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        res = list()
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            cells = [cell.get_text() for cell in cells]
            if not len(cells) == 7:
                continue
            elif cells[0] == 'RCP\xa0Average':
                continue
            poll_name, poll_date, poll_sample, poll_biden, poll_sanders, poll_gabbard, poll_spread = cells
            poll_biden, poll_sanders, poll_gabbard = (self._str_to_float(
                x) for x in (poll_biden, poll_sanders, poll_gabbard))
            res.append(Poll(poll_date, poll_sample, poll_sanders,
                       poll_biden, poll_gabbard, poll_spread))
            # logging.debug(f"{poll_name}, {poll_date}, {poll_sample}, {poll_biden}, {poll_sanders}, {poll_gabbard}, {poll_spread}")
        # logging.debug(res)
        return res

    def polls(self, table: int = 0) -> List[Poll]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the parsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[Poll] -- List of Poll namedtuples that were created from the
                table data.
        """
        return super().polls(table)

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.

        """
        polls = self.polls(loc)
        biden_total = sum((x.Biden for x in polls))
        sanders_total = sum((x.Sanders for x in polls))
        gabbard_total = sum((x.Gabbard for x in polls))
        table_name = "RealClearPolitics"
        number_field_width = 5
        name_field_width = 8
        res = (
            f"\n{table_name}\n"
            f"{'=' * len(table_name)}\n"
            f"{'Biden':>9}: {biden_total:.1f}\n"
            f"{'Sanders':>9}: {sanders_total:.1f}\n"
            f"{'Gabbard':>9}: {gabbard_total:.1f}\n"

        )
        print(res)


@dataclass
class NYTimes(Site):
    """NYTimes object.

    NYTimes is a custom class to parse a Web instance from the nytimes website.

    Variables:
        web: Web -- The web object stores the information needed to process
            the data.

    Methods:
        find_table: -> str -- Parses the Web object for table elements and
            returns the first one that it finds unless an integer representing
            the required table is passed.

        parse_rows: -> List[LeaderBoard] -- Parses a BeautifulSoup table element and
            returns the text found in the td elements as LeaderBoard namedtuples.

        polls: -> List[LeaderBoard] -- Does the parsing of the table and rows for you.
            It takes the table index number if given, otherwise parses table 0.

        stats: -- Formats the results from polls into a more user friendly
            representation:

            Example:

            NYTimes
            =================================

                               Pete Buttigieg
            ---------------------------------
            National Polling Average: 10%
                   Pledged Delegates: 25
            Individual Contributions: $76.2m
                Weekly News Coverage: 3

    """

    web: Web

    def parse_rows(self, table: Soup) -> List[LeaderBoard]:
        """Parses the row data from the html table.

        Arguments:
            table {Soup} -- Parses a BeautifulSoup table element and
                returns the text found in the td elements as LeaderBoard namedtuples.

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
            the table data.
        """
        res = list()
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if len(cells) != 5:
                continue

            poll_name = cells[0].find(name="span", class_="g-desktop").string.strip()
            cells = [cell.get_text().strip() for cell in cells[1:]]
            poll_average, poll_delegates, poll_contributions, poll_coverage = cells
            poll_delegates = self._str_to_int(poll_delegates)
            poll_coverage = self._str_to_int(poll_coverage[1:])
            res.append(LeaderBoard(poll_name, poll_average,
                       poll_delegates, poll_contributions, poll_coverage))
        return res

    def polls(self, table: int = 0) -> List[LeaderBoard]:
        """Parses the data

        The find_table and parse_rows methods are called for you and the table index
        that is passed to it is used to get the correct table from the soup object.

        Keyword Arguments:
            table {int} -- Does the pardsing of the table and rows for you.
                It takes the table index number if given, otherwise parses table 0.
                (default: {0})

        Returns:
            List[LeaderBoard] -- List of LeaderBoard namedtuples that were created from
                the table data.
        """
        return super().polls(table)

    def _candidate_report(self, candidate_info: LeaderBoard, report_width: int=33) -> str:
        field_names = ["National Polling Average", "Pledged Delegates",
                       "Individual Contributions", "Weekly News Coverage"]
        longest_label = max((len(label) for label in field_names))
        label_column = longest_label+2
        data_column = report_width - label_column
        assert data_column > 0
        res = (
            f"\n{candidate_info.Candidate.rjust(report_width)}\n{'-' * report_width}\n"
            f"{field_names[0].rjust(longest_label)}: {candidate_info.Average}\n"
            f"{field_names[1].rjust(longest_label)}: {candidate_info.Delegates}\n"
            f"{field_names[2].rjust(longest_label)}: {candidate_info.Contributions}\n"
            f"{field_names[3].rjust(longest_label)}: {candidate_info.Coverage}\n"
        )
        return res

    def stats(self, loc: int = 0):
        """Produces the stats from the polls.

        Keyword Arguments:
            loc {int} -- Formats the results from polls into a more user friendly
            representation.
        """
        REPORT_WIDTH = 33
        polls = self.polls(loc)
        res = (
            f"NYTimes\n"
            f"{'='* REPORT_WIDTH}\n"
        )
        for poll in polls:
            res += self._candidate_report(poll, REPORT_WIDTH)
        print(res)


def gather_data():
    rcp_file = File("RealClearPolitics.html")
    rcp_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_realclearpolitics.html"
    )
    rcp_web = Web(rcp_url, rcp_file)
    rcp = RealClearPolitics(rcp_web)
    rcp.stats(3)

    nyt_file = File("nytimes.html")
    nyt_url = (
        "https://bites-data.s3.us-east-2.amazonaws.com/2020-03-10_nytimes.html"
    )
    nyt_web = Web(nyt_url, nyt_file)
    nyt = NYTimes(nyt_web)
    nyt.stats()


if __name__ == "__main__":
    gather_data()
