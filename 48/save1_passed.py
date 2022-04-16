import os
import urllib.request
import re
from itertools import groupby

book_line_expression = r"(?P<month>\d\d)-(?P<day>\d\d)\s+(?:\d\d):(?:\d\d)\s+(?:\w+)\s+(?:\w+)\s+(?P<bookinfo>.*)\s+(?:\d\d)-(?:\d\d)\s+(?:\d\d):(?:\d\d)\s+(?:\w+)\s+(?:\w+)\s+(?P<destination>.*)"

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'
urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def keyfunc(x):
    return (x[0], x[1])


def create_chart():
    with open(LOG) as body:
        text = body.read()
        books = re.findall(book_line_expression, text)
        new_books = [entry[:-1] for entry in books if "sending to slack" in entry[-1]]
        sorted_books = sorted(new_books, key=keyfunc)
        for date, days_books in groupby(sorted_books, keyfunc):
            print(f"{date[0]}-{date[1]} ", sep='', end='')
            for curent_book in days_books:
                if "python" in curent_book[2].lower():
                    print(PY_BOOK, sep='', end='')
                else:
                    print(OTHER_BOOK, sep='', end='')
            print()


if __name__ == "__main__":
    create_chart()
