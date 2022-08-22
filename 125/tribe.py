from collections import Counter
import re
from typing import Optional, Tuple, List, Counter as CounterType

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
# static copy
TIM_BLOG = ('https://bites-data.s3.us-east-2.amazonaws.com/'
            'tribe-mentors-books.html')
MIN_COUNT = 3

title_re = re.compile(
    r"http(?:s?)://(?:www.)?amazon.com/(?P<title>[^/]*)/dp/(?:.*)")


def load_page() -> str:
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content: Optional[str] = None) -> List[Tuple[str, int]]:
    """Make a BeautifulSoup object loading in content,
       find all links that contain AMAZON, extract the book title
       (stripping spacing characters), and count them.
       Return a list of (title, count) tuples where
       count is at least MIN_COUNT
    """
    if content is None:
        content = load_page()
    # code here ...
    res: CounterType[str]
    soup = BeautifulSoup(content, 'html.parser')
    titles = (" ".join(tag.stripped_strings)
              for tag in soup.find_all('a') if 'amazon' in tag.get('href'))
    res = Counter(titles)
    return [(title, count) for title, count in res.most_common() if count >= MIN_COUNT]
