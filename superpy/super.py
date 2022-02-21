# Imports
import argparse
import csv
import datetime
from datetime import date, datetime, timedelta
import sys
import pytest

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
today = date.today()
# print(datetime)
# print(date(0, 12, 31))
# print(today)
# print(datetime.today())


# print(time)
# '%Y-%m-%d'

# met timedelta kun je ook teruggaan in de tijd, num_days is dan negatief
# zo kun je terug of vooruit, naar gisteren (--yesterday) of morgen (--tomorrow)
def advance_time(num_days):
    advanced_date = today + timedelta(num_days)
    print(
        f"OK\nThe current date is {today}.\nThe advanced date is {advanced_date}.")


def parse_arguments():
    if len(sys.argv) == 1:
        print("Please enter at least one more argument.")
    if len(sys.argv) >= 2:
        if sys.argv[1] == "report":
            print("report")
        if sys.argv[1] == "--advance-time":
            missing_argument = len(sys.argv) == 2
            if missing_argument:
                print(
                    'Please enter the number of days, e.g.: "python super.py --advance-time 2."')
            else:
                num_days = int(sys.argv[2])
                advance_time(num_days)


if __name__ == "__main__":
    parse_arguments()

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
