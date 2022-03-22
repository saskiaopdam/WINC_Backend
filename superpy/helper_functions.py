# Imports
import csv
import argparse
from datetime import datetime, date, timedelta
from calendar import monthrange
import time
from time import strptime

today = date.today()
yesterday = date.today() - timedelta(1)


def get_product_list():
    # get product list from products.csv
    product_list = []
    with open('products.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            product = row['product']
            if product not in product_list:
                product_list.append(product)
    product_list.sort()
    return product_list


def update_products(product):
    # called from record_event()
    # updates products.csv
    product_list = get_product_list()
    if product not in product_list:
        with open('products.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow({product})
        print("product added to products.csv")


def get_product_stock(product, date):
    def total_sellable():
        # total_sellable: total amount of the product bought and not expired up to (and including) the given date
        total_sellable = 0
        with open('bought.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product and row['date'] <= date.strftime("%Y-%m-%d") and row['exp'] > date.strftime("%Y-%m-%d"):
                    total_sellable += int(row['count'])
            return total_sellable

    def total_sold():
        # total_sold: total amount of the product sold up to (and including the given date)
        total_sold = 0
        with open('sold.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product'] == product and row['date'] <= date.strftime("%Y-%m-%d"):
                    total_sold += int(row['count'])
            return total_sold

    total_sellable = total_sellable()
    total_sold = total_sold()
    product_stock = total_sellable - total_sold
    return product_stock


def print_total_stock():
    # called from stock()

    product_list = get_product_list()
    no_products = len(product_list) == 0
    if no_products:
        print("No products, cannot calculate stock.")
    else:
        print("Sellable - not expired - products at current date:")
        for product in product_list:
            today = date.today()
            stock = get_product_stock(product, today)
            print(f"{product}: {stock}")


def get_period_result(filename, args):
    # called from revenue() and profit()
    month = args.month
    year = args.year

    with open(filename) as csvfile:
        month = strptime(month, '%b').tm_mon
        year = strptime(year, '%Y').tm_year
        _, days_in_month = monthrange(year, month)

        start_date = date(year, month, 1).strftime('%Y-%m-%d')
        end_date = date(
            year, month, days_in_month).strftime('%Y-%m-%d')

        reader = csv.DictReader(csvfile)
        result = 0
        for row in reader:
            if row['date'] >= start_date and row['date'] <= end_date:
                result += float(row['price'])
        return result


def record_event(filename, args):
    # called from buy() and sell()
    action = args.subcommand
    product = args.product
    date = args.date
    count = args.count

    def record_action():
        data = [args.product, args.date,
                args.price, args.exp, args.count]
        # exclude future date
        date = args.date
        if date > date.today():
            print(
                f"You can't {action} a product on a future date ({date}).")
        else:
            # append data to csv file
            with open(filename, 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)
                print(f"event added to {filename}")

    if action == "buy":
        update_products(product)
        record_action()

    if action == "sell":
        # check stock
        stock = get_product_stock(product, date)
        # if not enough stock:
        if stock < count:
            print(f"Can't sell {count}. On stock: {stock}.")
        # if enough stock:
        else:
            record_action()


def valid_date(date_string):
    # called from buy() and sell()
    """
    Regex vs. strptime():

    Validation with regex allows for a check against the format: '^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$' (<year between 0000 and 9999> - <month between 01 and 12> - <day between 01 and 31>). However, this does not include a check for existing combinations of year, month and day.

    Validation with datetime.strptime() includes a build-in check against the format YYYY-mm-dd, as well as a build-in check for existing dates, throwing an error when the combination of year, month and day does not exist (e.g. 2022-02-29 or 2022-04-31). Date strings entered without a zero padding are converted to ones with zero padding.

    For this reason, .strptime() is preferable.

    """
    try:
        # return existing date in YYYY-MM-DD format
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        msg = f"invalid date format: '{date_string}'. Should be an existing date in the format YYYY-MM-DD.".format(
            date_string)
        raise argparse.ArgumentTypeError(msg)
