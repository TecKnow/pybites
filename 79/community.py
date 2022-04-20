from csv import DictReader
from unittest import result

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
        decoded content"""
    r = requests.get(CSV_URL)
    list_of_lines = r.text.splitlines()
    csv_dicts = DictReader(list_of_lines)
    data = dict()
    for entry in csv_dicts:
        data.setdefault(entry['tz'], set()).add(entry['id'])
    for entry in data:
        data[entry] = len(data[entry])
    return data


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    NAME_COLUMN_WIDTH = 21
    data = get_csv()
    sorted_data = sorted(data.items())
    for row in sorted_data:
        print(f"{row[0].ljust(21)}| {'+' * row[1]}")
