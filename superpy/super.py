# Imports
import argparse
import csv
import datetime
from datetime import date, datetime, timedelta
import sys
import os
import pytest
import itertools

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
current_date = date.today()
today = current_date
yesterday = today + timedelta(-1)
tomorrow = today + timedelta(1)


def advance(num_days):
    advanced_date = today + timedelta(num_days)
    print(
        f"OK\nThe current date is {today}.\nThe advanced date is {advanced_date}.")


def buy(product_name, buy_date, buy_price, expiration_date, count):
    with open('buy.csv', 'a') as csvfile:
        data = [product_name, buy_date, buy_price, expiration_date, count]
        buy_id = id(data)
        writer = csv.writer(csvfile)
        writer.writerow([buy_id] + data)

    print(
        f"OK\n'{buy_id} {product_name} {buy_date} {buy_price} {expiration_date} {count}' now added to buy.csv.")


def report(data, date):
    # if date == "yesterday":
    #     print(data, yesterday)
    # elif date == "today":
    #     print(data, today)
    # elif date == "tomorrow":
    #     print(data, tomorrow)
    if date == "yesterday":
        with open('buy.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            row_count = 0
            match_count = 0
            print(f"Products bought yesterday ({yesterday}):")
            for row in reader:
                row_count += 1
                if row['buy_date'] == str(yesterday):
                    match_count += 1
                    print(
                        f"id: {row['id']}, product_name: {row['product_name']}, buy_date: {row['buy_date']}, buy_price: {row['buy_price']}, expiration_date: {row['expiration_date']}, count: {row['count']}")
            if row_count == 0:
                print("0\n(no products bought so far).")
            if row_count > 0 and match_count == 0:
                print("0")


def main():

    # top-level parser
    parser = argparse.ArgumentParser(
        prog='SuperPy', description='Keep track of the supermarket inventory and produce reports on various kinds of data')
    subparsers = parser.add_subparsers(dest='command')

    # parser for the "advance" command
    advance_parser = subparsers.add_parser(
        'advance', help='advance the current date with a number of days')
    advance_parser.add_argument('--days', type=int, help='number of days')

    # parser for the "buy" command
    buy_parser = subparsers.add_parser(
        'buy', help='record information about a bought product')
    buy_parser.add_argument('--name', help='product name', required=True)
    buy_parser.add_argument('--date', help='buy date', required=True)
    buy_parser.add_argument('--price', type=float,
                            help='buy price', required=True)
    buy_parser.add_argument('--exp', help='expiration date', required=True)
    buy_parser.add_argument('--count', type=int,
                            help='product count', required=True)

    # parser for the "report" command
    report_parser = subparsers.add_parser(
        'report', help='print a report to the terminal')
    report_parser.add_argument('--data', help='data to be printed')
    report_parser.add_argument(
        '--date', help='selected date', choices=["yesterday", "today", "tomorrow"])

    args = parser.parse_args()

    if args.command == 'advance':
        advance(args.days)
    if args.command == 'buy':
        buy(args.name, args.date,
            args.price, args.exp, args.count)
    if args.command == 'report':
        report(args.data, args.date)


if __name__ == "__main__":
    main()

# Tested function


def function_X():
    return None

# Python classes
