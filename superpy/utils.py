# Imports
import argparse
from datetime import date, datetime, timedelta
import csv

# Variables
current_date = date.today()
today = current_date
yesterday = today + timedelta(-1)


# Functions


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


def advance(args):
    advanced_date = today + timedelta(args.days)
    print(
        f"OK\nThe current date is {today}.\nThe advanced date is {advanced_date}.")


def buy(args):
    with open('buy.csv', 'a') as csvfile:
        data = [args.name, args.buy_date,
                args.price, args.exp_date, args.count]
        buy_id = id(data)
        writer = csv.writer(csvfile)
        writer.writerow([buy_id] + data)

    print(
        f"OK\n'{buy_id} {args.name} {args.buy_date} {args.price} {args.exp_date} {args.count}' has been added to buy.csv.")


def report(args):
    data = args.data
    day = args.day

    def get_date(day):
        if day == "yesterday":
            return yesterday
        elif day == "today":
            return today
    date = get_date(day)
    # if date == "yesterday":
    #     print(data, yesterday)
    # elif date == "today":
    #     print(data, today)
    # elif date == "tomorrow":
    #     print(data, tomorrow)

    def print_heading():
        print(f"{data.capitalize()} {day} ({date}):")
    print_heading()

    def print_data():
        # imlement choice of stdout (terminal or pdf)
        def print_inventory():
            with open('buy.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                row_count = 0
                match_count = 0
                product_list = []

                # def get_products():
                #     for product in len(product_list):
                #         print(product_list[product])

                for row in reader:
                    row_count += 1
                    prod_name = row['product_name']
                    count = row['count']
                    buy_price = row['buy_price']
                    exp_date = row['expiration_date']
                    if prod_name not in product_list:
                        product_list.append(prod_name)

                    if row['buy_date'] == str(date):
                        match_count += 1
                        print(
                            f"{prod_name}, {count}, {buy_price}, {exp_date}")

                print(product_list)
                products = ', '.join(product_list)
                print(f"Products offered: {products}")
                if row_count == 0:
                    print("0 (no products bought so far).")
                if row_count > 0 and match_count == 0:
                    print("0")

        def print_revenue():
            print("revenue data")

        def print_profit():
            print("profit data")

        if data == "inventory":
            print_inventory()
        if data == "revenue":
            print_revenue()
        if data == "profit":
            print_profit()

    print_data()
