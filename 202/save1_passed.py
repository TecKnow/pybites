import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
tmp = Path(os.getenv("TMP", "/tmp"))
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, newline='', encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        row_list = list(reader)
        row_list = [{"Bite": int(row["Bite"].split()[1][:-1]), "Difficulty": float(row["Difficulty"])} for row in
                    row_list if row["Difficulty"] != "None"]
        row_list = list(sorted(row_list, key=lambda row: row["Difficulty"], reverse=True))
        return [row["Bite"] for row in row_list[:N]]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
