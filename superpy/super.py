# Imports
import argparse
from argparse import ArgumentParser

from datetime import date, timedelta

# from setting_date import set_date
from recording import record
from reporting import report
# from purchase import buy

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    # create a parser and subparsers
    parser = ArgumentParser(
        usage="python %(prog)s [-h | --help] <command> <arguments>", description="The following options and subcommands are available in SuperPy:", epilog="For help on a specific subcommand, see 'python super.py <command> -h'.", formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(
        title="subcommands", prog="python super.py", dest="subcommand")

    # define a decorator to turn a function into a subcommand
    def subcommand(subparser_args=[], parent=subparsers):
        def decorator(func):
            parser = parent.add_parser(
                func.__name__, description=func.__doc__, help=func.__doc__)
            for args, kwargs in subparser_args:
                # print(f"args: {args}\nkwargs: {kwargs}")
                parser.add_argument(*args, **kwargs)
            parser.set_defaults(func=func)
        return decorator

    # helper function taking arguments
    def argument(*args, **kwargs):
        return args, kwargs

    # @subcommand([argument("No arguments", help="No arguments")])
    @subcommand()
    def nothing(args):
        """print 'Nothing special!'"""
        print("Nothing special!")

    @subcommand()
    def something(args):
        """print 'Something special!'"""
        print("Something special!")

    @subcommand([argument("-d", help="debug mode", action="store_true")])
    # e.g. args = ("-d",) kwargs = {help="debug mode", action="store_true"}
    def test(args):
        """print all arguments"""
        print(args)

    @subcommand([argument("-f", "--filename", help="a thing with a filename")])
    def filename(args):
        """print filename"""
        print(args.filename)

    @subcommand([argument("name", help="name")])
    def name(args):
        """print name"""
        print(args.name)

    @subcommand()
    def today(args):
        """print today's date"""
        today = date.today()
        print(today)

    @subcommand()
    def yesterday(args):
        """print yesterday's date"""
        today = date.today()
        yesterday = today - timedelta(1)
        print(yesterday)

    @subcommand([argument("num_days", type=int, help="number of days, positive or negative"), argument("arg2", type=int, help="arg2 help")])
    def set_today(args):
        """set current date +/- a number of days"""
        today = date.today()
        num_days = args.num_days
        new_today = today + timedelta(num_days)
        print(new_today)

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

    # dispatch the subcommand
    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    main()

# Tested function - running tests with pytest


def function_X():
    return None

# Python classes - debugging

# Extra - rich module, matplot
