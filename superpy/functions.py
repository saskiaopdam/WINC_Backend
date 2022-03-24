# Imports
import csv
import argparse
from datetime import datetime, date, timedelta


# Subcommand functions
def today(args):
    today = date.today()
    print(today)


def yesterday(args):
    yesterday = date.today() - timedelta(1)
    print(yesterday)


def days_ago(args):
    today = date.today()
    days_ago = args.days
    past_date = today - timedelta(days_ago)

    if args.txt:
        # export to text file
        filename = "date.txt"

        with open(filename, 'w') as textfile:
            textfile.write(str(past_date))

        print(f"{past_date} exported to date.txt")

    else:
        print(f"{past_date}")


def buy(args):

    # exclude future purchase date
    if args.date > date.today():
        print("purchase not recorded - the purchase date may not be a future date")

    else:
        # append data to csv file
        filename = "purchases.csv"
        data = [args.product, args.date, args.price,
                args.expiration, args.count]

        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

        print(f"purchase recorded in purchases.csv")


def valid_date(date_string):
    # make sure the entered date has the YYYY-MM-DD format
    # make sure the entered date is an existing date
    """
    Regex vs. strptime():

    You could use a regex: '^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'

    However, this would ensure the right format, but would not prevent a non-existing date like 2022-02-29 or 2022-04-31 from being recorded.

    The strptime() method on the other hand will throw an error if the combination of year, month and day does not exist.
    """
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        msg = f"{date_string} - should be an existing date in the format YYYY-MM-DD.".format(
            date_string)
        raise argparse.ArgumentTypeError(msg)
