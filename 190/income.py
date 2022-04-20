import os
from bisect import insort
from pathlib import Path
from urllib.request import urlretrieve
from xml.etree import ElementTree

# import the countries xml file
tmp = Path(os.getenv("TMP", "/tmp"))
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/countries.xml',
        countries
    )

NS = {"wb": "http://www.worldbank.org"}


def _parse_country_xml(xml=countries):
    tree = ElementTree.parse(countries)
    root = tree.getroot()
    country_elements = root.findall("wb:country", NS)
    for country_element in country_elements:
        country_name = country_element.find("wb:name", NS).text
        country_income_level = country_element.find("wb:incomeLevel", NS).text
        yield country_name, country_income_level


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    result = dict()
    for country_name, country_income_level in _parse_country_xml(xml=countries):
        target_list = result.setdefault(country_income_level, list())
        insort(target_list, country_name)
    return result
