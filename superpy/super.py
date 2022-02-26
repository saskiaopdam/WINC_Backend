# Imports
import argparse
import csv
import datetime
from datetime import date, datetime, timedelta
import sys
import os
import pytest

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
today = date.today()

# advance the current date (today) with a number of days, either forwards (num_days is positive) or backwards (num_days is negative)


def advance(num_days):
    advanced_date = today + timedelta(num_days)
    print(
        f"OK\nThe current date is {today}.\nThe advanced date is {advanced_date}.")


data = []


def buy(product_name, count):
    # stdout_fileno = sys.stdout
    # input = product_name
    # sys.stdout = open('Output.csv', 'w')
    # sys.stdout.write(input)
    # sys.stdout.close()
    # sys.stdout = stdout_fileno
    # print(
    #     f"OK\n{product_name.capitalize()} written to Output.csv.")
    # header = ['product_name', 'count']

    # input = [product_name, count]
    # data.append(input)
    data = [product_name, count]

    with open('buy.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        # for arg in sys.argv:
        # writer.writerow(header)
        writer.writerow(data)
        # buywriter.writerow(arg)
    print(
        f"OK\n'{product_name} {count}' added to buy.csv.")

    # fieldnames = ['product_name', 'count']
    # rows = [{'product_name': product_name, 'count': count},
    #         {'product_name': 'orange', 'count': 30}]

    # with open('buy.csv', 'w', newline='') as csvfile:
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     # for arg in sys.argv:
    #     writer.writeheader()
    #     writer.writerows(rows)
    #     # buywriter.writerow(arg)
    # print(
    #     f"OK\n'{product_name} {count}' written to buy.csv.")


def report(data):
    print(data)


def handle_user_input():
    # parse command line arguments

    # top-level parser
    parser = argparse.ArgumentParser(prog='SuperPy')
    subparsers = parser.add_subparsers(dest='command')

    # parser for the "advance" command
    parser_advance = subparsers.add_parser(
        'advance', help='advance the current date with a number of days')
    parser_advance.add_argument('num_days', type=int)

    # parser for the "buy" command
    parser_buy = subparsers.add_parser(
        'buy', help='record information about a bought product')
    parser_buy.add_argument('product_name')
    parser_buy.add_argument('count', type=int)

    # parser for the "report" command
    parser_report = subparsers.add_parser('report', help='print report')
    parser_report.add_argument('data', type=str,
                               help='data selection to print out')

    args = parser.parse_args()

    if args.command == 'advance':
        advance(args.num_days)
    if args.command == 'buy':
        buy(args.product_name, args.count)
    if args.command == 'report':
        report(args.data)

    # if len(sys.argv) == 1:
    #     print("Please enter at least one more argument.")
    # if len(sys.argv) >= 2:
    #     if sys.argv[1] == "report":
    #         print("report")
    #     if sys.argv[1] == "--advance-time":
    #         missing_argument = len(sys.argv) == 2
    #         if missing_argument:
    #             print(
    #                 'Please enter the number of days, e.g.: "python super.py --advance-time 2."')
    #         else:
    #             num_days = int(sys.argv[2])
    #             advance_time(num_days)

    # user input
    # stdin_fileno = sys.stdin

    # # # Keeps reading from stdin and quits only if the word 'exit' is there
    # # # This loop, by default does not terminate, since stdin is open
    # for line in stdin_fileno:
    #     # Remove trailing newline characters using strip()
    #     if 'exit' == line.strip():
    #         print('Found exit. Terminating the program')
    #         exit(0)
    #     else:
    #         print('Message from sys.stdin: ---> {} <---'.format(line))

    # write the command line arguments to a txt file:

    # Save the current stdout so that we can revert sys.stdou after we complete
    # our redirection
    # stdout_fileno = sys.stdout

    # # sample_input = ['Hi', 'Hello from AskPython', 'exit']
    # sample_input = sys.argv

    # # Redirect sys.stdout to the file
    # sys.stdout = open('Output.csv', 'w')

    # for ip in sample_input[1:]:
    #     # Prints to the redirected stdout (Output.txt)
    #     sys.stdout.write(ip + '\n')
    #     # Prints to the actual saved stdout handler
    #     stdout_fileno.write(ip + '\n')

    # # Close the file
    # sys.stdout.close()
    # # Restore sys.stdout to our old saved file handler
    # sys.stdout = stdout_fileno


if __name__ == "__main__":
    handle_user_input()

# in terminal: python super.py hello world
# print(sys.argv)  # ['super.py', 'hello', 'world']
# print(sys.argv[1:])  # ['hello', 'world']
# print(sys.argv[0])  # super.py
# # The name of the program is: super.py
# print("This is the name of the program:", sys.argv[0])
# print("Argument List: ", str(sys.argv))  # ['super.py', 'hello', 'world']
# print("Arguments count:", len(sys.argv))

# n = len(sys.argv)

# for i in range(0, n):
#     print(sys.argv[i])

# if sys.argv[1] == "report":
#     print("The first argument is: " + "report")

# Tested function


def function_X():
    return None

# Python classes
