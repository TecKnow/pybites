from collections import Counter
from pprint import pprint

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()



# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    by_year = Counter([row['automaker'] for row in data if row['year']==year])
    return by_year.most_common(1)[0][0]



def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = {row['model'] for row in data if row['automaker'] == automaker and row['year'] == year}
    return models

if __name__ == "__main__":
    res = get_models('Volkswagen', 2008)
    print(res)