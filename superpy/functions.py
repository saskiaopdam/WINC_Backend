# Imports
import csv
import argparse
from datetime import datetime, date, timedelta
from time import strptime
from calendar import monthrange


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

    # read "result.txt" to see which result was calculated recently (revenue or profit)
    with open("result.txt", 'r') as textfile:
        result = textfile.read()

        # calculate this result for the date n days ago
        if result == "revenue":
            revenue = day_result("sales.csv", past_date)
            print("Your last calculation was revenue.")
            print(f"Revenue {days_ago} day ago ({past_date})):") if days_ago == 1 else print(
                f"Revenue {days_ago} days ago ({past_date}):")
            print(revenue)
        if result == "profit":
            revenue = day_result("sales.csv", past_date)
            cost = day_result("purchases.csv", past_date)
            profit = revenue - cost
            print("Your last calculation was profit.")
            print(f"Profit {days_ago} day ago ({past_date}):") if days_ago == 1 else print(
                f"Profit {days_ago} days ago ({past_date}):")
            print(profit)
        # if no result (revenue or profit) has been calculated so far, just print the past date
        if not result:
            print(past_date)


# helper function for products()
def product_list():
    product_list = []
    with open('purchases.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            product = row['product']
            if product not in product_list:
                product_list.append(product)
    product_list.sort()
    return product_list


def products(args):
    offered_products = product_list()
    no_products = len(offered_products) == 0

    if no_products:
        print("no products")
    else:
        if args.csv:
            # export to csv file
            filename = "products.csv"

            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                for product in offered_products:
                    writer.writerow([product])

            print("offered products exported to products.csv")

        else:
            print("\n".join(offered_products))


# helper function for stock() and sell()
def product_stock(product, date):
    def amount_sellable():
        # bought and not expired products
        amount_sellable = 0
        with open('purchases.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product and row['date'] <= date.strftime("%Y-%m-%d") and row['expiration'] > date.strftime("%Y-%m-%d"):
                    amount_sellable += int(row['count'])
            return amount_sellable

    def amount_sold():
        amount_sold = 0
        with open('sales.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product and row['date'] <= date.strftime("%Y-%m-%d"):
                    amount_sold += int(row['count'])
            return amount_sold

    amount_sellable = amount_sellable()
    amount_sold = amount_sold()
    product_stock = amount_sellable - amount_sold
    return product_stock


def stock(args):
    offered_products = product_list()
    no_products = len(offered_products) == 0

    today = date.today()

    if no_products:
        print("no products to calculate stock")
    else:
        if args.csv:
            # export to csv file
            filename = "stock.csv"

            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                for product in offered_products:
                    stock = product_stock(product, today)
                    writer.writerow([product, stock])

            print("current stock exported to stock.csv")

        else:
            for product in offered_products:
                stock = product_stock(product, today)
                print(f"{product}: {stock}")


# helper function for result()
def period_result(filename, period):

    with open(filename) as csvfile:
        # find number of days in entered month
        month = strptime(period, '%B %Y').tm_mon
        year = strptime(period, '%B %Y').tm_year
        _, days_in_month = monthrange(year, month)

        # find the start- and end_date of this month
        start_date = date(year, month, 1).strftime('%Y-%m-%d')
        end_date = date(
            year, month, days_in_month).strftime('%Y-%m-%d')

        reader = csv.DictReader(csvfile)
        result = 0
        for row in reader:
            if row['date'] >= start_date and row['date'] <= end_date:
                result += float(row['price'])
        return result


# helper function for result()
def day_result(filename, day):

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        result = 0
        for row in reader:
            if row['date'] == str(day):
                result += float(row['price'])
        return result


# helper function for revenue() and profit()
def result(args):
    # the subcommand is either "revenue" or "profit"
    subcommand = args.subcommand

    if args.today is None and args.yesterday is None and args.month is None:
        print(
            f"please enter an option - see 'python super.py {subcommand} -h'")
    else:
        if args.today:
            today = date.today()
            revenue = day_result("sales.csv", today)
            cost = day_result("purchases.csv", today)
            profit = revenue - cost
            if subcommand == "revenue":
                print(f"Revenue today ({today}):")
                print(revenue)
            if subcommand == "profit":
                print(f"Profit today ({today}):")
                print(profit)
        if args.yesterday:
            yesterday = date.today() - timedelta(1)
            revenue = day_result("sales.csv", yesterday)
            cost = day_result("purchases.csv", yesterday)
            profit = revenue - cost
            if subcommand == "revenue":
                print(f"Revenue yesterday ({yesterday}):")
                print(revenue)
            if subcommand == "profit":
                print(f"Profit yesterday ({yesterday}):")
                print(profit)
        if args.month:
            period = args.month
            revenue = period_result("sales.csv", period)
            cost = period_result("purchases.csv", period)
            profit = revenue - cost
            if subcommand == "revenue":
                print(f"Revenue {period}:")
                print(revenue)
            if subcommand == "profit":
                print(f"Profit {period}:")
                print(profit)

        # write "revenue" or "profit" to text file for days_ago() to read
        filename = "result.txt"

        with open(filename, 'w') as textfile:
            textfile.write(subcommand)


def revenue(args):
    result(args)


def profit(args):
    result(args)


def buy(args):
    # exclude future purchase date
    if args.date > date.today():
        purchase_date = args.date.strftime("%Y-%m-%d")
        print(
            f"purchase not recorded - {purchase_date} is a future date - enter past or current date")

    else:
        # append data to csv file
        filename = "purchases.csv"
        data = [args.product, args.date, args.price,
                args.expiration, args.count]

        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

        print(f"purchase recorded in purchases.csv")


def sell(args):
    product = args.product
    date = args.date
    count = args.count
    # product_stock() excludes expired products
    stock = product_stock(product, date)

    # exclude future sale date
    if args.date > date.today():
        sale_date = args.date.strftime("%Y-%m-%d")
        print(
            f"sale not recorded - {sale_date} is a future date - enter past or current date")

    else:
        # exclude buying more than on stock
        if stock < count:
            print(
                f"sale not recorded - can't sell {count} with {stock} in stock")

        else:
            # append data to csv file
            filename = "sales.csv"
            data = [args.product, args.date, args.price, args.count]

            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)

            print(f"sale recorded in sales.csv")


def valid_month(date_string):
    # called from "revenue" - type=valid_month

    # make sure the entered month has the b-Y format
    try:
        return datetime.strptime(date_string, "%b-%Y").strftime("%B %Y")
    except ValueError:
        msg = f"'{date_string}' - should be month-year, e.g. jan-2020".format(
            date_string)
        raise argparse.ArgumentTypeError(msg)


def valid_date(date_string):
    # called from "buy" - type=valid_date

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


# idea: finish the function singular():
def singular(product_name):
    # called from "buy" - type=singular
    # make sure the entered product name is singular, not plural
    """
    This will prevent names like "apple" and "apples" being recorded as purchases of a different product in purchases.csv.

    Three subcommands use the records in purchases.csv to make their calculations:

    - "products"
    - "stock"
    - "sell"

    For them to work correctly, it's important that doubles are excluded.
    """
    # try - except block like the one in valid_date()
    # return singular noun
    # use nltk package? (from nltk.stem import WordNetLemmatizer)
