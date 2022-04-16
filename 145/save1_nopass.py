from collections import namedtuple
from datetime import datetime

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")

date_parse_format_string = "%Y-%m-%d"
date_to_day_of_year_format_string = "%j"


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

    """
    id        date element  data_value
    0  USW00094889  2014-11-12    TMAX          22
    1  USC00208972  2009-04-29    TMIN          56
    2  USC00200032  2008-05-26    TMAX         278
    3  USC00205563  2005-11-11    TMAX         139
    4  USC00200230  2014-02-27    TMAX        -106
    """
    df = pd.read_csv(DATA_FILE)
    df.columns = [col.lower() for col in df]
    df["date"] = df["date"].apply(lambda x: datetime.strptime(x, date_parse_format_string))
    df["day"] = df["date"].apply(lambda x: int(x.strftime(date_to_day_of_year_format_string)))
    df = df[df["day"] != 366]
    historical_data = df[df["date"].dt.year != 2015]
    comparison_data = df[df["date"].dt.year == 2015]
    max_temps_raw = historical_data[(historical_data["element"] == "TMAX")]
    max_temps = max_temps_raw.groupby(by=["id", "day"])['data_value'].max()
    print(max_temps.describe())


if __name__ == "__main__":
    high_low_record_breakers_for_2015()
