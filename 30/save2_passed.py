import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import statistics
from pprint import pprint

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    with open(MOVIE_DATA, newline='') as csvfile:
        movies = dict()
        reader = csv.DictReader(csvfile)
        for line in reader:
            try:
                title = line["movie_title"]
                year = int(line["title_year"])
                score = float(line["imdb_score"])
                if year >= 1960:
                    movies.setdefault(line["director_name"], list()).append(Movie(title=title, year=year, score=score))
            except ValueError:
                pass
        return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    return round(statistics.mean((movie.score for movie in movies)), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    director_scores = ((key, calc_mean_score(value)) for key, value in directors.items() if len(value)>= MIN_MOVIES)
    director_scores_sorted = sorted(director_scores, key=lambda x: x[1], reverse=True)
    return director_scores_sorted


if __name__ == "__main__":
    pprint(get_average_scores(get_movies_by_director()))
