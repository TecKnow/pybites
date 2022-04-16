import os
from urllib.request import urlretrieve

import pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, 'order_data.xlsx')
if not os.path.isfile(EXCEL):
    urlretrieve(
        'https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx',
        EXCEL
    )


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(excel, sheet_name="SalesOrders")


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df["Year"] = df["OrderDate"].dt.year
    sales_region_year = df[["Year", "Region", "Total"]
                           ].groupby(["Year", "Region"]).aggregate(sum)
    return sales_region_year


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    rep_sales = df[["Rep", "Total"]].groupby("Rep").aggregate(sum)
    rep_sales_sorted = rep_sales.sort_values(["Total"], ascending=False)
    return rep_sales_sorted.head(1).to_records()[0]


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    most_sold_items = df[["Item", "Units"]].groupby("Item").aggregate(sum)
    most_sold_items_sorted = most_sold_items.sort_values(
        ["Units"], ascending=False)
    return most_sold_items_sorted.head(1).to_records()[0]
