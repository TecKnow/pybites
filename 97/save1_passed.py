from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, 'html.parser')
    holiday_table = soup.find(name="table", class_="list-table")
    print(holiday_table)
    holiday_list = holiday_table.find_all(name="tr", class_=lambda t: t in ("holiday", "regional", "publicholiday"))
    for holiday in holiday_list:
        holiday_name = holiday.find_all(name="td")[3].find(name="a").get_text()
        holiday_datetime = holiday.find(name="time")["datetime"]
        holiday_date_month = holiday_datetime.split('-')[1]
        holidays[holiday_date_month].append(holiday_name)
    return holidays


if __name__ == "__main__":
    from pprint import pprint
    res = get_us_bank_holidays()
    pprint(res)