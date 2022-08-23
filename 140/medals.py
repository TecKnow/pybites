import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"
header = "Year,City,Sport,Discipline,Athlete,Country,Gender,Event,Medal".split(',')


def athletes_most_medals(data: str = data) -> pd.Series:
    t = pd.read_csv(data, dtype={
        "City": "category",
        "Sport": "category",
        "Discipline": "category",
        "Athlete": "string",
        "Gender": "category",
        "Event": "string",
        "Medal": "category",
        "Country": "category",
        })
    m = t.groupby(["Gender", "Athlete"])["Medal"].count()
    mm = m.loc['Men'].nlargest(1).append(m.loc["Women"].nlargest(1))
    return mm


if __name__ == "__main__":
    athletes_most_medals()