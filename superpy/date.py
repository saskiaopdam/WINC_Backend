import argparse
# import datetime
from datetime import date, datetime, timedelta

current_date = date.today()
today = current_date
yesterday = today + timedelta(-1)
# tomorrow = today + timedelta(1)


def advance(args):
    advanced_date = today + timedelta(args.days)
    print(
        f"OK\nThe current date is {today}.\nThe advanced date is {advanced_date}.")


def valid_date(date_string):
    """
    Function ensures that the 'buy_date' and 'exp_date' arguments match the following format:
    - YYYY-MM-DD (e.g. 2022-03-01)
    """

    # regex check
    # if not re.match('^(\d{4}-\d{2}-\d{2}|yesterday|today)$', value):
    #     raise argparse.ArgumentTypeError(
    #         "must be in the form YYYY-MM-DD, yesterday, or today".format(value))
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        # msg = "Not a valid date: {0!r}. Must be in the form YYYY-MM-DD.".format(
        #     date_string)
        msg = f"Incorrect data format: '{date_string}'. Should be YYYY-MM-DD.".format(
            date_string)
        raise argparse.ArgumentTypeError(msg)
