import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap.strip() == "n/a":
        return 0
    cap = cap.strip()
    cap = cap[1:] if cap.startswith("$") else cap
    if cap.endswith("M"):
        cap = cap[:-1]
        cap = float(cap)
        return cap
    elif cap.endswith("B"):
        cap = cap[:-1]
        cap = float(cap) * 1000
        return cap


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_entries = [x for x in data if x["industry"] == industry]
    industry_cap = sum(
        _cap_str_to_mln_float(x["cap"]) for x in industry_entries)
    return round(float(industry_cap), 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    return sorted(
        data, key=lambda x: _cap_str_to_mln_float(x["cap"]),
        reverse=True)[0]["symbol"]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    filtered_data = [x for x in data if x["sector"] != 'n/a']
    num_stocks_by_industry = Counter([x["sector"] for x in filtered_data])
    sorted_stocks_by_industry = num_stocks_by_industry.most_common()
    max_num_stocks = sorted_stocks_by_industry[0][0]
    min_num_stocks = sorted_stocks_by_industry[-1][0]
    return (max_num_stocks, min_num_stocks)
