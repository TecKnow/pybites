from enum import Enum
from datetime import datetime
from collections import Counter
from typing import List, Optional, Union, overload
import typing
from contextlib import suppress


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @overload
    @classmethod
    def get_d_parse_formats(cls) -> List[str]:
        pass

    @overload
    @classmethod
    def get_d_parse_formats(cls, val: int) -> str:
        pass

    @classmethod
    def get_d_parse_formats(cls, val: Optional[int] = None) -> Union[str, List[str]]:
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str: str) -> List[DateFormat]:
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(
                date_str, d_parse_fmt)  # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates: List[str]) -> List[str]:
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Allowed/supported date formats are defined in a DF enum class.
    """
    # complete this method
    date_type_frequency: typing.Counter[DateFormat] = Counter()
    for date in dates:
        date_type_frequency.update(_maybe_DateFormats(date))
    (most_common_format,
     most_common_count), (second_most_common_format,
                          second_most_common_count) = date_type_frequency.most_common(2)
    winning_format = most_common_format
    if most_common_count == second_most_common_count:
        if most_common_format == DateFormat.NONPARSABLE:
            winning_format = second_most_common_format
        elif second_most_common_format == DateFormat.NONPARSABLE:
            winning_format = most_common_format
        else:
            raise InfDateFmtError(
                f"Ambiguous date format, {most_common_format} and {second_most_common_format}"
                f"are tied for highest frequency at {most_common_count}")
    if winning_format == DateFormat.NONPARSABLE:
        raise InfDateFmtError(
            "Too many unparseable dates to infer a date format")
    winning_format_str: str = DateFormat.get_d_parse_formats(
        winning_format.value)
    res = list()
    for date in dates:
        normalized_date_string = "Invalid"
        with suppress(ValueError):
            normalized_date_string = datetime.strptime(
                date, winning_format_str).strftime("%Y-%m-%d")
        res.append(normalized_date_string)
    return res
