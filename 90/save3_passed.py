from collections import Counter, defaultdict, namedtuple
import csv

import requests

LineRecord = namedtuple('LineRecord', 'Season, Episode, Character, Line')

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def make_line_records(content):
    season_lines = content.splitlines()
    season_lines.pop(0)
    season_reader = csv.reader(season_lines)
    line_records = tuple(map(LineRecord._make, season_reader))
    line_records = tuple(x._replace(Line=tuple(x.Line.split())) for x in line_records)
    return line_records


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    line_records = make_line_records(content)
    character_dict = defaultdict(Counter)
    for line_record in line_records:
        character_dict[line_record.Character][line_record.Episode] += len(line_record.Line)
    return character_dict
