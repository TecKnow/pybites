import pandas as pd

"""
columns:

['Category', 'Item', 'Serving Size', 'Calories', 'Calories from Fat',
 'Total Fat', 'Total Fat (% Daily Value)', 'Saturated Fat',
 'Saturated Fat (% Daily Value)', 'Trans Fat', 'Cholesterol',
 'Cholesterol (% Daily Value)', 'Sodium', 'Sodium (% Daily Value)',
 'Carbohydrates', 'Carbohydrates (% Daily Value)', 'Dietary Fiber',
 'Dietary Fiber (% Daily Value)', 'Sugars', 'Protein',
 'Vitamin A (% Daily Value)', 'Vitamin C (% Daily Value)',
 'Calcium (% Daily Value)', 'Iron (% Daily Value)']
"""

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    result_row = df[df["Calories"] == df["Calories"].max()]
    return result_row.iloc[0].loc["Item"]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    eligible_foods = df[df["Calories"] > 0]
    if excl_drinks:
        eligible_foods = eligible_foods[~eligible_foods["Category"].isin(
            ['Coffee & Tea', 'Beverages'])]
    eligible_foods['Fiber Ratio'] = eligible_foods['Protein'] / \
        eligible_foods["Calories"].astype(float)
    top_foods = eligible_foods.sort_values("Fiber Ratio", ascending=False)[0:5]
    return top_foods["Item"].tolist()
