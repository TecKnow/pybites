from collections import namedtuple
from itertools import groupby
import csv
from datetime import datetime
import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")
RECORD = namedtuple("Record", "station_id date year day reading_type temp")

date_parse_format_string = "%Y-%m-%d"
date_to_day_of_year_format_string = "%j"


def _get_csv_data():
    df = pd.read_csv(DATA_FILE)
    df.columns = [col.lower() for col in df]
    return df.to_dict("records")


def _parse_csv_data(csv_data):
    """
    id        date element  data_value
    0  USW00094889  2014-11-12    TMAX          22
    1  USC00208972  2009-04-29    TMIN          56
    2  USC00200032  2008-05-26    TMAX         278
    3  USC00205563  2005-11-11    TMAX         139
    4  USC00200230  2014-02-27    TMAX        -106
    """
    station_data = list()
    for row in csv_data:
        station_id = row["id"]
        date = datetime.strptime(row["date"], date_parse_format_string).date()
        year = int(date.year)
        day_of_year = int(date.strftime(date_to_day_of_year_format_string))
        reading_type = "max" if row["element"] == "TMAX" else "min" if row["element"] == "TMIN" else None
        reading_value = int(row["data_value"])
        new_record = RECORD(station_id=station_id, date=date, year=year, day=day_of_year, reading_type=reading_type,
                            temp=reading_value)
        station_data.append(new_record)
    return tuple(station_data)


def _remove_leap_days(station_data):
    return tuple(x for x in station_data if x.day != 366)


def _separate_historic_data(station_data):
    current_data = tuple(x for x in station_data if x.year == 2015)
    historic_data = tuple(x for x in station_data if x.year != 2015)
    return current_data, historic_data


def _record_sort_key(record):
    return (record.station_id, record.day, record.year)


def _separate_highs_lows(station_data):
    sorted_station_data = tuple(sorted(station_data, key=_record_sort_key))
    highs = tuple(x for x in sorted_station_data if x.reading_type == "max")
    lows = tuple(x for x in sorted_station_data if x.reading_type == "min")
    return (highs, lows)


def _groupby_sort_key(record):
    return (record.station_id, record.day)


def _historic_record_highs(station_data_highs):
    results = list()
    for k, g in groupby(station_data_highs, key=_groupby_sort_key):
        group = tuple(g)
        max_found = max(group, key=lambda x: x.temp)
        results.append(max_found)
    return tuple(results)


def _historic_record_lows(station_data_lows):
    results = list()
    for k, g in groupby(station_data_lows, key=_groupby_sort_key):
        group = tuple(g)
        results.append(min(group, key=lambda x: x.temp))
    return tuple(results)


def _current_record_breaking_highs(current_data, historic_highs):
    historic_high_dict = dict()
    for row in historic_highs:
        historic_high_dict.setdefault(row.station_id, dict())[row.day] = row
    results = list()
    for row in current_data:
        if row.temp > historic_high_dict[row.station_id][row.day].temp:
            results.append(row)
    return tuple(results)


def _current_record_breaking_lows(current_data, historic_lows):
    historic_low_dict = dict()
    for row in historic_lows:
        historic_low_dict.setdefault(row.station_id, dict())[row.day] = row
    results = list()
    for row in current_data:
        if row.temp < historic_low_dict[row.station_id][row.day].temp:
            results.append(row)
    return tuple(results)


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value

    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    csv_data = _get_csv_data()
    station_data = _parse_csv_data(csv_data)
    trimmed_data = _remove_leap_days(station_data)
    current_data, historic_data = _separate_historic_data(trimmed_data)
    highs, lows = _separate_highs_lows(historic_data)
    historic_record_highs = _historic_record_highs(highs)
    historic_record_lows = _historic_record_lows(lows)
    current_record_breaking_highs = _current_record_breaking_highs(current_data, historic_record_highs)
    current_record_breaking_lows = _current_record_breaking_lows(current_data, historic_record_lows)
    highest_record_breaking_high = max(current_record_breaking_highs, key=lambda x: x.temp)
    lowest_record_breaking_low = min(current_record_breaking_lows, key=lambda x: x.temp)
    highest_high_station = STATION(highest_record_breaking_high.station_id, highest_record_breaking_high.date,
                                   highest_record_breaking_high.temp / 10)
    lowest_low_station = STATION(lowest_record_breaking_low.station_id, lowest_record_breaking_low.date,
                                 lowest_record_breaking_low.temp / 10)
    return (highest_high_station, lowest_low_station)


if __name__ == "__main__":
    from pprint import pprint

    pprint(high_low_record_breakers_for_2015())
