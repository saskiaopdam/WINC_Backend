# Imports
import csv
import argparse
from datetime import datetime, date, timedelta
from time import strptime
from calendar import monthrange
import xlsxwriter
from beautifultable import BeautifulTable


# Subcommand functions

# helper function for today()
def read_today_str():
    with open('today.txt', 'r') as textfile:
        today = textfile.read()
    return today


# helper function for yesterday() and advance_today()
def get_today_obj():
    today = read_today_str()
    today_obj = datetime.strptime(today, "%Y-%m-%d").date()
    return today_obj


def today(args):
    today = read_today_str()
    if today == "":
        # save the current date in "today.txt"
        with open('today.txt', 'w') as textfile:
            current_date = date.today().strftime("%Y-%m-%d")
            textfile.write(current_date)

        print(f"Today: {current_date}")
    else:
        print(f"Today: {today}")


def yesterday(args):
    today = get_today_obj()
    yesterday = today - timedelta(1)
    print(f"Yesterday: {yesterday}")


def advance_today(args):
    today = get_today_obj()
    days = args.days
    new_today = today - timedelta(days)

    # save the new today in "today.txt"
    with open('today.txt', 'w') as textfile:
        new_today_str = new_today.strftime("%Y-%m-%d")
        textfile.write(new_today_str)

    print(
        f"Today is advanced with {days} days from {today} to {new_today_str}.")


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
        print("no products offered")
    else:
        if args.csv:
            # export to csv file
            filename = "products.csv"

            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["product"])
                for product in offered_products:
                    writer.writerow([product])

            print("offered products exported to products.csv")

        elif args.excel:
            # export to excel file
            workbook = xlsxwriter.Workbook('products.xlsx')
            worksheet = workbook.add_worksheet()

            # add a bold format
            bold = workbook.add_format({'bold': True})

            # define data
            products = ()

            for product in offered_products:
                products = products + (product,)

            # start from first cell
            row = 0
            col = 0

            # write headers
            worksheet.write(row, 0, 'product', bold)

            # go to second row
            row = 1
            col = 0

            # write data out row by row
            for product in (products):
                worksheet.write(row, col,     product)
                row += 1

            workbook.close()

            print("offered products exported to products.xlsx")

        else:
            table = BeautifulTable()
            for product in offered_products:
                table.rows.append([product])
            table.columns.header = ["product"]
            table.columns.alignment["product"] = BeautifulTable.ALIGN_LEFT
            table.set_style(BeautifulTable.STYLE_DOTTED)
            print(table)


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

    today = get_today_obj()

    if no_products:
        print("no products to calculate stock")
    else:
        if args.csv:
            # export to csv file
            filename = "stock.csv"

            with open(filename, 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["product", "stock"])
                for product in offered_products:
                    stock = product_stock(product, today)
                    writer.writerow([product, stock])

            print("current stock exported to stock.csv")

        elif args.excel:
            # export to excel file
            workbook = xlsxwriter.Workbook('stock.xlsx')
            worksheet = workbook.add_worksheet()

            # add a bold format
            bold = workbook.add_format({'bold': True})

            # define data
            total_stock = ()

            for product in offered_products:
                stock = product_stock(product, today)
                total_stock = total_stock + ([product, stock],)

            # start from first cell
            row = 0
            col = 0

            # write headers
            worksheet.write(row, col, 'product', bold)
            worksheet.write(row, col + 1, 'stock', bold)

            # go to second row
            row = 1
            col = 0

            # write data out row by row
            for product, amount in (total_stock):
                worksheet.write(row, col,     product)
                worksheet.write(row, col + 1, amount)
                row += 1

            workbook.close()

            print("current stock exported to stock.xlsx")

        else:
            print(f"Stock today ({today}):")
            table = BeautifulTable()
            for product in offered_products:
                stock = product_stock(product, today)
                table.rows.append([product, stock])
            table.columns.header = ["product", "stock"]
            table.columns.alignment["product"] = BeautifulTable.ALIGN_LEFT
            table.columns.alignment["stock"] = BeautifulTable.ALIGN_RIGHT
            table.columns.padding_left["stock"] = 5
            table.set_style(BeautifulTable.STYLE_DOTTED)
            print(table)


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
                result += float(row['price'])*float(row['count'])
        return result


# helper function for result()
def day_result(filename, day):

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        result = 0
        for row in reader:
            if row['date'] == str(day):
                result += float(row['price'])*float(row['count'])
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
            today = read_today_str()
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
            today = get_today_obj()
            yesterday = today - timedelta(1)
            # yesterday = date.today() - timedelta(1)
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

        # # write "revenue" or "profit" to text file for days_ago() to read
        # filename = "result.txt"

        # with open(filename, 'w') as textfile:
        #     textfile.write(subcommand)


def revenue(args):
    result(args)


def profit(args):
    result(args)


def buy(args):
    # exclude future purchase date
    if args.date > date.today():
        purchase_date = args.date.strftime("%Y-%m-%d")
        print(
            f"purchase not recorded - {purchase_date} is a future date - please enter past or current date")

    # exclude past or current expiration date
    if args.expiration <= date.today():
        expiration_date = args.date.strftime("%Y-%m-%d")
        print(
            f"purchase not recorded - {expiration_date} is a past or current date - please enter a future date")

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
            f"sale not recorded - {sale_date} is a future date - please enter past or current date")

    else:
        # exclude selling more than is in stock on the selling date
        if stock < count:
            print(f"{product.capitalize()} in stock on {date}: {stock}.")
            print(
                f"Sale not recorded - can't sell {count} with {stock} in stock.")

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
    # called from "buy" and "sell" - type=valid_date

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
        msg = f"{date_string} - should be an existing date in the format YYYY-MM-DD".format(
            date_string)
        raise argparse.ArgumentTypeError(msg)


def lowercase(string):
    return string.lower()


# idea: finish the function singular():
def singular(product_name):
    # called from "buy" and "sell" - type=singular

    # make sure the entered product name is singular, not plural
    """
    This will prevent names like "apple" and "apples" being recorded as purchases / sales of a different product in purchases.csv / sales.csv.

    Three subcommands use the records in purchases.csv and sales.csv to make calculations on specific products:

    - "products"
    - "stock"
    - "sell"

    For them to work correctly, it's important that doubles are excluded.
    Otherwise reports on products and stock will include "apple" as well as "apples" as different products, while in fact they are the same. The sell() function checks how much of the specified product is in stock. It could calculate a lower amount when searching for "apple" while "apples" are also in stock.
    """
    # try - except block like the one in valid_date()
    # return singular noun
    # use nltk package? (from nltk.stem import WordNetLemmatizer)
