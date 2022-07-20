from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = 'https://bites-data.s3.us-east-2.amazonaws.com/packt.html'
CONTENT = requests.get(PACKT).text
DOTD_MAIN_CLASS = "dotd-main-book"
DOTD_SUMMARY_CLASS = "dotd-main-book-summary"
DOTD_IMAGE_CLASS = "dotd-main-book-image"

Book = namedtuple('Book', 'title description image link')


def get_book():
    from pprint import pprint
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')
    # print(soup.prettify())
    free_area = soup.find(class_=DOTD_MAIN_CLASS)
    free_title = free_area.find(class_="dotd-title").text.strip()
    description_area = free_area.find(class_=DOTD_SUMMARY_CLASS)
    description_div = description_area.find(
        "div", id=lambda attr: not attr, class_=lambda attr: not attr)
    description_string = description_div.text.strip()
    image_div = free_area.find(class_=DOTD_IMAGE_CLASS)
    book_link = image_div.find('a')
    book_url = book_link.get("href").strip()
    image_tag = book_link.find('img')
    image_url = image_tag.get('src').strip()
    return Book(free_title, description_string, image_url, book_url)


if __name__ == "__main__":
    get_book()
