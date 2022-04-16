from collections import Counter, namedtuple
import csv
import re
from copy import deepcopy
from itertools import islice

import requests

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')


# csv parsing code provided so this Bite can focus on the parsing

def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


characters = list(load_data())


# start coding

def most_popular_characters(characters=characters, top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    local_characters = deepcopy(characters)
    local_characters = [x._replace(appearances=int(x.appearances)) for x in local_characters if x.appearances]
    popular = sorted(local_characters, key=lambda x: x.appearances, reverse=True)
    popular = islice(popular, top)
    popular = (x.name for x in popular)
    return list(popular)


def max_and_min_years_new_characters(characters=characters):
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv
       characters, or the 'year' attribute of the namedtuple, return a tuple
       of (max_year, min_year)
    """
    local_characters = deepcopy(characters)
    local_characters = [x._replace(year=int(x.year)) for x in local_characters if x.year]
    characters_by_year = Counter(x.year for x in local_characters).most_common()
    return characters_by_year[0][0], characters_by_year[-1][0]


def get_percentage_female_characters(characters=characters):
    """Get the percentage of female characters as percentage of all genders
       over all appearances.
       Ignore characters that don't have gender ('sex' attribue) set
       (in your characters data set you should only have Male, Female,
       Agender and Genderfluid Characters.
       Return the result rounded to 2 digits
    """
    local_characters = deepcopy(characters)
    local_characters = [x for x in local_characters if x.sex]
    female_characters = [x for x in local_characters if x.sex == "Female Characters"]
    return round((len(female_characters) / len(local_characters)) * 100, 2)
