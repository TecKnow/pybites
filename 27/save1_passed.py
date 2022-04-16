import glob
import json
import os
from urllib.request import urlretrieve
import re

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    res = list()
    for file_name in files:
        with open(file_name) as file:
            movie_dict = json.load(file)
        movie_dict['Runtime'] = int(movie_dict['Runtime'].split()[0])
        res.append(movie_dict)
    return res


def get_single_comedy(movies):
    return [movie["Title"] for
            movie in movies if "Comedy" in movie['Genre']][0]


def get_movie_most_nominations(movies):
    nom_count_re = re.compile(r"(?P<nom_count>\d+) nominations")
    return sorted(movies,
                  key=lambda x: int(nom_count_re.search(x["Awards"]).group("nom_count")), reverse=True)[0][
        "Title"]


def get_movie_longest_runtime(movies):
    sorted_movies = sorted(movies, key=lambda x: x["Runtime"], reverse=True)
    return sorted_movies[0]["Title"]