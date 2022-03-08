# Imports
"""
- modules from the python standard library
- functions from programme files
"""
import argparse
import sys
from datetime import date

from utils import advance, buy, report, valid_date
# from report import report
# from date import valid_date, advance
# from trade import buy

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    # create the top-level parser
    def parse_args(args=sys.argv[1:]):
        parser = argparse.ArgumentParser(
            description="Programme to keep track of supermarket inventory and produce reports on inventory, revenue and profit.")
        subparsers = parser.add_subparsers()

        add_advance_subparser(subparsers)
        add_buy_subparser(subparsers)
        add_report_subparser(subparsers)

        return parser.parse_args(args)

    # create the parser for the "advance" command
    def add_advance_subparser(subparsers):
        parser = subparsers.add_parser(
            'advance', help='advance the current date with a number of days')
        parser.add_argument('days', type=int,
                            help='number of days')
        parser.set_defaults(func=advance)

    # create the parser for the "buy" command
    def add_buy_subparser(subparsers):
        parser = subparsers.add_parser(
            'buy', help='record information about a bought product')
        parser.add_argument('name', help='product name')
        parser.add_argument('buy_date', type=valid_date,
                            help='buy date - format: YYYY-MM-DD')
        parser.add_argument('price', type=float,
                            help='buy price')
        parser.add_argument(
            'exp_date', type=valid_date, help='expiration date - format: YYYY-MM-DD')
        parser.add_argument('count', type=int,
                            help='product count')
        parser.set_defaults(func=buy)

    # create the parser for the "report" command
    def add_report_subparser(subparsers):
        parser = subparsers.add_parser(
            'report', help='print a report to the terminal')
        parser.add_argument(
            'data', choices=["inventory", "revenue", "profit"], help='data to be printed')
        parser.add_argument(
            'day', choices=["yesterday", "today"], help='selected date')
        parser.add_argument(
            '--stdout', choices=["terminal", "pdf"], help='standard output to terminal or pdf')
        parser.set_defaults(func=report)

    # parse_args()
    if len(sys.argv[1:]) == 0:
        print("No arguments to process.")
    else:
        args = parse_args()
        args.func(args)


if __name__ == "__main__":
    main()

# Tested function


def function_X():
    return None

# Python classes
