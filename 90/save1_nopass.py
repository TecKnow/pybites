from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_season_dict(season):
    season_file = get_season_csv_file(season)
    season_lines = season_file.splitlines()
    season_reader = csv.DictReader(season_lines)
    season_entries = list(season_reader)
    for entry in season_entries:
        del entry['Season']
        del entry['Line']
    return season_entries


def make_character_dict(season_entries):
    character_dict = defaultdict(Counter)
    for line in season_entries:
        (Character, Episode) = (line["Character"], line["Episode"])
        character_dict[Character][Episode] += 1
    return character_dict


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    season_dict = get_season_dict(content)
    character_dict = make_character_dict(season_dict)
    return character_dict


if __name__ == "__main__":
    print(make_character_dict((get_season_dict(1))))
