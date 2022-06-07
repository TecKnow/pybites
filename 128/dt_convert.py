from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    parse_string = "%d %b, %Y"
    date_object = datetime.strptime(date, parse_string)
    return THIS_YEAR - date_object.year


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
        Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
        To enforce the use of datetime's strptime / strftime (over slicing)
        the tests check if a ValueError is raised for invalid day/month/year
        ranges (no need to code this, datetime does this out of the box)"""
    eu_format_string = "%d/%m/%Y"
    us_format_string = "%m/%d/%Y"
    date_object = datetime.strptime(date, eu_format_string)
    return date_object.strftime(us_format_string)