# Imports
import argparse
from datetime import date, timedelta

from helper_functions import get_product_list, get_total_stock, valid_date, record_data
# from setting_date import set_date
# from reporting import report

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    # create top-level parser for the command-line arguments
    def create_parser():
        parser = argparse.ArgumentParser(
            usage="python %(prog)s [option] <subcommand> [arguments]", description="The following options and subcommands are available in SuperPy:", epilog="For help on a specific subcommand, enter 'python super.py <subcommand> -h'.")
        return parser
    parser = create_parser()

    # create sub-level parsers for the subcommands
    def create_subparsers():
        subparsers = parser.add_subparsers(
            title="subcommands", prog="python super.py", dest="subcommand", metavar="available actions to set time, record data and report on data")
        return subparsers
    subparsers = create_subparsers()

    # define decorator to turn a function into a subcommand
    """
    Each function is associated with a subcommand with the same name.
    This way, when entering e.g. 'nothing' on the command-line, the function nothing() is executed.
    """
    def subcommand(subcommand_args=[], parent=subparsers):
        def decorator(function):
            parser = parent.add_parser(
                function.__name__, description=function.__doc__, help=function.__doc__)
            for args, kwargs in subcommand_args:
                parser.add_argument(*args, **kwargs)
                # see test() function below for illustration of args and kwargs
            parser.set_defaults(subcmdfunc=function)
        return decorator

    # define helper function taking arguments
    def argument(*args, **kwargs):
        return args, kwargs

    # subcommand arguments
    # stock_args = [argument("day", choices=["today", "yesterday"])]

    set_today_args = [argument("num_days", type=int, help="number of days, positive or negative"), argument(
        "arg2", type=int, help="arg2 help")]

    buy_args = [argument("product", help="product name"),
                argument("date", help="purchase date - YYYY-MM-DD", type=valid_date), argument("price", help="purchase price - floating-point number", type=float), argument("exp", help="expiration date - YYYY-MM-DD"), argument("count", help="product count - integer", type=int)]

    sell_args = [argument("product", help="product name"),
                 argument("date", help="selling date - YYYY-MM-DD", type=valid_date), argument("price", help="selling price - floating-point number", type=float), argument("exp", help="expiration date - YYYY-MM-DD"), argument("count", help="product count - integer", type=int)]

    offer_args = [argument("product", help="product name")]

    # calling decorator, passing functions
    # @subcommand()
    # def today(args):
    #     """print today's date"""
    #     today = date.today()
    #     print(today)

    # @subcommand()
    # def yesterday(args):
    #     """print yesterday's date"""
    #     yesterday = date.today() - timedelta(1)
    #     print(yesterday)

    @subcommand()
    def products(args):
        """print offered products"""
        product_list = get_product_list()
        no_products = len(product_list) == 0
        if no_products:
            print("no products")
        else:
            products = "\n".join(product_list)
            print(products)

    # @subcommand(stock_args)
    @subcommand()
    def stock(args):
        """print stock of all offered products"""
        get_total_stock(args)

    @subcommand(set_today_args)
    def set_today(args):
        """set current date +/- a number of days"""
        today = date.today()
        num_days = args.num_days
        new_today = today + timedelta(num_days)
        print(new_today)

    @subcommand(buy_args)
    def buy(args):
        """record buying event in bought.csv"""
        filename = "bought.csv"
        record_data(filename, args)

    @subcommand(sell_args)
    def sell(args):
        """record selling event in sold.csv"""
        filename = "sold.csv"
        record_data(filename, args)

    # create the parser for the "set_date" command

    def add_set_date_subparser(subparsers):
        parser = subparsers.add_parser(
            'set_date', description='Command to set the current date.', help='set current date')
        parser.add_argument(
            'direction', choices=["backwards", "forwards"], help='direction of date setting')
        parser.add_argument('num_days', type=int,
                            help='number of days')
        parser.set_defaults(func=set_date)

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

    def parse_args():
        args = parser.parse_args()
        if args.subcommand is None:
            parser.print_help()
        else:
            # execute subcommand function
            args.subcmdfunc(args)
    parse_args()


if __name__ == "__main__":
    main()

# Tested function - running tests with pytest


def function_X():
    return None

# Python classes - debugging

# Extra - rich module, matplot
