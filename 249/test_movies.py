import os
import random
import string

import pytest

from movies import MovieDb

salt = ''.join(
    random.choice(string.ascii_lowercase) for i in range(20)
)
DB = os.path.join(os.getenv("TMP", "/tmp"), f'movies_{salt}.db')
# https://www.imdb.com/list/ls055592025/

NEW_ITEM = ("Vertigo", 1958, 8.3)
DATA = [
    ("The Godfather", 1972, 9.2),
    ("The Shawshank Redemption", 1994, 9.3),
    ("Schindler's List", 1993, 8.9),
    ("Raging Bull", 1980, 8.2),
    ("Casablanca", 1942, 8.5),
    ("Citizen Kane", 1941, 8.3),
    ("Gone with the Wind", 1939, 8.1),
    ("The Wizard of Oz", 1939, 8),
    ("One Flew Over the Cuckoo's Nest", 1975, 8.7),
    ("Lawrence of Arabia", 1962, 8.3),
]
TABLE = 'movies'


@pytest.fixture
def db():
    # instantiate MovieDb class using above constants
    # do proper setup / teardown using MovieDb methods
    # https://docs.pytest.org/en/latest/fixture.html (hint: yield)

    mdb = MovieDb(DB, DATA, TABLE)
    mdb.init()
    yield mdb
    mdb.drop_table()


# write tests for all MovieDb's query / add / delete
def test_query_total(db):
    res = db.query("The Godfather", 1972, 9.2)
    assert res == [(1, "The Godfather", 1972, 9.2)]


def test_query_exact_title(db):
    res = db.query("The Godfather")
    assert res == [(1, "The Godfather", 1972, 9.2)]

def test_query_partial_title(db):
    res = db.query("odfath")
    assert res == [(1, "The Godfather", 1972, 9.2)]


def test_query_year(db):
    res = db.query(year=1942)
    assert len(res) == 1
    assert res == [(5, "Casablanca", 1942, 8.5)]

def test_query_score(db):
    res = db.query(score_gt=9.3)
    assert len(res) == 0
    res = db.query(score_gt=9.2)
    assert res == [(2, 'The Shawshank Redemption', 1994, 9.3)]

def test_add(db):
    db.add(*NEW_ITEM)
    res = db.query(*NEW_ITEM)
    assert res == [(11, *NEW_ITEM)]

def test_delete(db):
    res = db.query("Raging Bull")
    assert len(res) == 1
    id, *details = res[0]
    assert details == ["Raging Bull", 1980, 8.2]
    db.delete(id)
    res = db.query("Raging Bull")
    assert len(res) == 0

