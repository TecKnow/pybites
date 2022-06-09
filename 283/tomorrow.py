from datetime import date, timedelta


def tomorrow(today=None):
    # Your code goes here
    today = date.today() if today is None else today
    tomrrow_delta = timedelta(days=1)
    tomorrow_datetime = today + tomrrow_delta
    return tomorrow_datetime
