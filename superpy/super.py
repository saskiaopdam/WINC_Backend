# Imports
import argparse
from datetime import date, timedelta

from helper_functions import get_product_list, print_total_stock, get_period_result, valid_date, record_event

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
    result_args = [argument("month", help="month - e.g. Jan"),
                   argument("year", help="year - e.g. 2020")]

    set_today_args = [
        argument("num_days", type=int, help="number of days, positive or negative")]

    event_args = [argument("product", help="product name"),
                  argument("date", help="purchase date - YYYY-MM-DD", type=valid_date), argument("price", help="purchase price - floating-point number", type=float), argument("exp", help="expiration date - YYYY-MM-DD"), argument("count", help="product count - integer", type=int)]

    # calling decorator, passing functions
    @ subcommand()
    def today(args):
        """print today's date"""
        today = date.today()
        print(today)

    @ subcommand()
    def yesterday(args):
        """print yesterday's date"""
        yesterday = date.today() - timedelta(1)
        print(yesterday)

    @ subcommand()
    def products(args):
        """print offered products"""
        product_list = get_product_list()
        no_products = len(product_list) == 0
        if no_products:
            print("no products")
        else:
            products = "\n".join(product_list)
            print(products)

    @ subcommand()
    def stock(args):
        """print current stock of all offered products"""
        print_total_stock()

    @ subcommand(result_args)
    def revenue(args):
        """print revenue for given time period"""
        revenue = get_period_result("sold.csv", args)
        print(revenue)

    @ subcommand(result_args)
    def profit(args):
        """print profit for given time period"""
        revenue = get_period_result("sold.csv", args)
        cost = get_period_result("bought.csv", args)
        profit = revenue - cost
        print(profit)

    # I can see no point in a function to advance-time the current date by 2 days, as specified in the assignment. Instead, I added two subcommands for the user to print the current and previous date (today() and yesterday()).

    # @ subcommand(set_today_args)
    # def set_today(args):
    #     """set current date +/- a number of days"""
    #     today = date.today()
    #     num_days = args.num_days
    #     new_today = today + timedelta(num_days)
    #     print(new_today)

    @ subcommand(event_args)
    def buy(args):
        """record buying event in bought.csv"""
        record_event("bought.csv", args)

    @ subcommand(event_args)
    def sell(args):
        """record selling event in sold.csv"""
        record_event("sold.csv", args)

    # parse arguments on command-line
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
