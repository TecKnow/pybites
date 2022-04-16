from collections import defaultdict
import csv 

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    lines = csv.DictReader(data.splitlines())
    for line in lines:
        countries.setdefault(line['country_code'], list()).append(' '.join((line['first_name'], line['last_name'])))
    return countries

print(group_names_by_country())
    