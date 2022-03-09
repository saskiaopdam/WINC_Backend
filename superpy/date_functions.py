# Imports
import argparse
from datetime import date, datetime, timedelta

# Variables
current_date = date.today()
today = current_date
yesterday = today + timedelta(-1)
# tomorrow = today + timedelta(1)

# Functions


def advance(args):
    advanced_date = today + timedelta(args.days)
    print(
        f"OK\nThe current date is {today}.\nThe advanced date is {advanced_date}.")


def valid_date(date_string):
    """
    Function ensures that the 'buy_date' and 'exp_date' arguments in the buy() function

    - match the format: YYYY-MM-DD (e.g. 2022-03-01)
    - correspond to an existing date (e.g. 2022-02-29 or 2022-04-31 being non existent)

    Regex vs. strptime():

    Validation with regex allows for a check against the format: '^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$' (<year between 0000 and 9999> - <month between 01 and 12> - <day between 01 and 31>). However, this does not include a check for existing combinations of year, month and day.

    Validation with datetime.strptime() includes a build-in check against the format YYYY-mm-dd, as well as a build-in check for existing dates, throwing an error when the combination of year, month and day does not exist (e.g. 2022-02-29 or 2022-04-31). Date strings entered without a zero padding are converted to ones with zero padding.

    For this reason, .strptime() is preferable.

    """
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        msg = f"invalid date format: '{date_string}'. Should be an existing date in the format YYYY-MM-DD.".format(
            date_string)
        raise argparse.ArgumentTypeError(msg)
