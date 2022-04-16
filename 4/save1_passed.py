import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET


# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding
root = ET.fromstring(content)
category_elems = root.findall('.//category')
cats = (cat.text for cat in category_elems)

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    cat_counter = Counter(cats)
    return cat_counter.most_common(n)