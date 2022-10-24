from typing import Iterable, List, Optional, Sequence, Tuple
from urllib.request import urlretrieve
import os
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html: Path = PYCON_HTML) -> Soup:
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup: Optional[Soup] = None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    if soup is None:
        soup = _get_soup()
    presenters_list = [''.join(elem.stripped_strings) for elem in soup.select(".speaker")]
    presenters = [presenter for presentation in presenters_list for presenter in presentation.split(",")]
    presenters = [presenter for presentation in presenters for presenter in presentation.split("/")]
    first_names = [first_name for first_name, *_ in [presenter.split() for presenter in presenters]]
    return first_names
    
def get_names_genders(names: Iterable[str]) -> List[Tuple[str, str]]:
    gender_detector = gender.Detector()
    return [(name, gender_detector.get_gender(name)) for name in names]

def get_percentage_of_female_speakers(first_names: Sequence[str])-> float:
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    d = gender.Detector()
    fem_names = [name for name in first_names if d.get_gender(name) in ("female", "mostly_female")]
    fem_fraction = len(fem_names)/ len(first_names)
    return round(fem_fraction * 100, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)
