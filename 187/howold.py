from dataclasses import dataclass
import datetime
import dateutil.parser


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    delta: datetime.timedelta = dateutil.parser.parse(
        movie.release_date) - dateutil.parser.parse(actor.born)
    age = delta / datetime.timedelta(days=365)
    return f"{actor.name} was {int(age)} years old when {movie.title} came out."
