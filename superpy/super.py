# Imports
import argparse
import sys

from date_setting import set_date
from recording import record
from reporting import report
from purchase import buy

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    # create the top-level parser
    def parse_args(args=sys.argv[1:]):
        parser = argparse.ArgumentParser(
            description="Command-line tool for keeping track of supermarket inventory.")
        subparsers = parser.add_subparsers()

        add_set_date_subparser(subparsers)
        add_record_subparser(subparsers)
        # add_buy_subparser(subparsers)
        add_report_subparser(subparsers)

        return parser.parse_args(args)

    # create the parser for the "set_date" command
    def add_set_date_subparser(subparsers):
        parser = subparsers.add_parser(
            'set_date', description='Command to set the current date.', help='set current date')
        parser.add_argument(
            'direction', choices=["backwards", "forwards"], help='direction of date setting')
        parser.add_argument('num_days', type=int,
                            help='number of days')
        parser.set_defaults(func=set_date)

    # create the parser for the "record" command
    def add_record_subparser(subparsers):
        parser = subparsers.add_parser(
            'record', description='Command to record entered data.', help='record entered data')
        parser.add_argument(
            'data', choices=["purchase", "sale"], help='data to be recorded')
        parser.set_defaults(func=record)

    # # create the parser for the "buy" command
    # def add_buy_subparser(subparsers):
    #     parser = subparsers.add_parser(
    #         'buy', description='Command to record purchase information in a file named bought.csv.', help='record purchase information in a file named bought.csv')
    #     parser.add_argument('product_name', help='name of the product')
    #     parser.add_argument('buy_date', type=valid_date,
    #                         help='purchase date - format: YYYY-MM-DD')
    #     parser.add_argument('buy_price', type=float,
    #                         help='purchase price')
    #     parser.add_argument(
    #         'expiration_date', type=valid_date, help='expiration date - format: YYYY-MM-DD')
    #     parser.add_argument('product_count', type=int,
    #                         help='product count')
    #     parser.set_defaults(func=buy)

    # create the parser for the "report" command
    def add_report_subparser(subparsers):
        parser = subparsers.add_parser(
            'report', description='Command to report on recorded data.', help='report on recorded data')
        parser.add_argument(
            'data', choices=["products", "inventory", "revenue", "profit"], help='data to be reported')
        # voor "products" alleen "data" argument, geen "date" argument!
        parser.add_argument(
            'day', choices=["yesterday", "today"], help='selected day')
        # parser.add_argument(
        #     '--stdout', choices=["terminal", "pdf"], help='standard output to terminal or pdf')
        parser.set_defaults(func=report)

    # parse_args()
    if len(sys.argv[1:]) == 0:
        print(
            "SuperPy running. Please enter a command. For help, enter: 'python super.py -h'.")
    else:
        args = parse_args()
        args.func(args)


if __name__ == "__main__":
    main()

# Tested function


def function_X():
    return None

# Python classes
