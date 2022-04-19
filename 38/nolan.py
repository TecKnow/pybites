import xml.etree.ElementTree as ET
from operator import itemgetter

# from OMDB
xmlstring = '''<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>'''  # noqa E501


def get_tree():
    """You probably want to use ET.fromstring"""
    return ET.fromstring(xmlstring)


def get_movies():
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    root_elem = get_tree()
    for movie in root_elem.findall("movie"):
        yield movie.get('title')


def get_movie_longest_runtime():
    """Call get_tree again and return the movie title for the movie with the longest
       runtime in minutes, for latter consider adding a _get_runtime helper"""
    longest_movie_tuple = max(_get_runtimes(), key=itemgetter(1))
    longest_movie_title = longest_movie_tuple[0]
    return longest_movie_title


def _get_runtime(movie_elem: ET.Element) -> int:
    runtime_str = movie_elem.get('runtime')
    runtime_elements = runtime_str.split()
    runtime_minutes = int(runtime_elements[0])
    return runtime_minutes


def _get_runtimes():
    root_elem = get_tree()
    for movie in root_elem.findall("movie"):
        yield movie.get("title"), _get_runtime(movie)


if __name__ == "__main__":
    print(get_movie_longest_runtime())
