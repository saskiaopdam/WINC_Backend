# Imports
import argparse


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    # Import subcommand functions
    from functions import today, yesterday, days_ago, buy, valid_date

    # Create the top-level parser
    parser = argparse.ArgumentParser(
        usage="python %(prog)s", epilog="For subcommand help, enter 'python super.py <subcommand> -h'.")
    subparsers = parser.add_subparsers(
        title="subcommands", prog="python super.py", dest="subcommand")

    # Create the parser for the "today" subcommand
    parser_today = subparsers.add_parser(
        "today", description="show today's date and exit", help="show today's date and exit")
    parser_today.set_defaults(func=today)

    # Create the parser for the "yesterday" subcommand
    parser_yesterday = subparsers.add_parser(
        "yesterday", description="show yesterday's date and exit", help="show yesterday's date and exit")
    parser_yesterday.set_defaults(func=yesterday)

    # Create the parser for the "days_ago" subcommand
    parser_days_ago = subparsers.add_parser(
        "days_ago", description="show the date n days ago and exit", help="show the date n days ago and exit")
    parser_days_ago.add_argument("days", type=int, help="number of days")
    parser_days_ago.add_argument(
        "-txt", action="store_const", const="date.txt", help="export the past date to date.txt")
    parser_days_ago.set_defaults(func=days_ago)

    # Create the parser for the "buy" subcommand
    parser_buy = subparsers.add_parser(
        "buy", description="record a purchase in purchases.csv and exit", help="record a purchase in purchases.csv and exit")
    parser_buy.add_argument("product", help="product name")
    parser_buy.add_argument("date", type=valid_date,
                            help="purchase date - YYYY-MM-DD")
    parser_buy.add_argument("price", type=float,
                            help="purchase price - floating point number")
    parser_buy.add_argument("expiration", type=valid_date,
                            help="expiration date - YYYY-MM-DD")
    parser_buy.add_argument("count", type=int, help="product count - integer")
    parser_buy.set_defaults(func=buy)

    # Parse the arguments and call whatever function was selected
    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    main()
