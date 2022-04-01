# Imports
import argparse


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():

    # Import subcommand functions
    from functions import today, yesterday, advance_today, products, stock, revenue, profit, buy, sell, valid_month, valid_date, lowercase

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

    # Create the parser for the "advance_today" subcommand
    parser_advance_today = subparsers.add_parser(
        "advance_today", description="advance 'today' with n days and exit", help="advance 'today' with n days and exit")
    parser_advance_today.add_argument("days", type=int, help="number of days")
    parser_advance_today.set_defaults(func=advance_today)

    # Create the parser for the "products" subcommand
    parser_products = subparsers.add_parser(
        "products", description="show the offered products and exit", help="show the offered products and exit")
    parser_products.add_argument(
        "-csv", action="store_const", const="products.csv", help="export the offered products to products.csv")
    parser_products.add_argument(
        "-excel", action="store_const", const="products.xlsx", help="export the offered products to products.xlsx")
    parser_products.set_defaults(func=products)

    # Create the parser for the "stock" subcommand
    parser_stock = subparsers.add_parser(
        "stock", description="show the current stock and exit", help="show the current stock and exit")
    parser_stock.add_argument(
        "-csv", action="store_const", const="stock.csv", help="export the current stock to stock.csv")
    parser_stock.add_argument(
        "-excel", action="store_const", const="stock.xlsx", help="export the current stock to stock.xlsx")
    parser_stock.set_defaults(func=stock)

    # Create the parser for the "revenue" subcommand
    parser_revenue = subparsers.add_parser(
        "revenue", description="show the revenue for period x and exit", help="show the revenue for period x and exit")
    parser_revenue.add_argument(
        "-today", action="store_const", const="today", help="show today's revenue")
    parser_revenue.add_argument(
        "-yesterday", action="store_const", const="yesterday", help="show yesterday's revenue")
    parser_revenue.add_argument(
        "-month", type=valid_month,
        help="show revenue of a month - e.g. jan-2022")
    parser_revenue.set_defaults(func=revenue)

    # Create the parser for the "profit" subcommand
    parser_profit = subparsers.add_parser(
        "profit", description="show the profit for period x and exit", help="show the profit for period x and exit")
    parser_profit.add_argument(
        "-today", action="store_const", const="today", help="show today's profit")
    parser_profit.add_argument(
        "-yesterday", action="store_const", const="yesterday", help="show yesterday's profit")
    parser_profit.add_argument(
        "-month", type=valid_month,
        help="show profit of a month - e.g. jan-2022")
    parser_profit.set_defaults(func=profit)

    # Create the parser for the "buy" subcommand
    parser_buy = subparsers.add_parser(
        "buy", description="record a purchase in purchases.csv and exit", help="record a purchase in purchases.csv and exit")
    # idea: add type=singular to the "product" argument
    parser_buy.add_argument("product", type=lowercase,
                            help="product name - singular noun")
    parser_buy.add_argument("date", type=valid_date,
                            help="purchase date - YYYY-MM-DD")
    parser_buy.add_argument("price", type=float,
                            help="purchase price - floating point number")
    parser_buy.add_argument("expiration", type=valid_date,
                            help="expiration date - YYYY-MM-DD")
    parser_buy.add_argument("count", type=int, help="product count - integer")
    parser_buy.set_defaults(func=buy)

    # Create the parser for the "sell" subcommand
    parser_sell = subparsers.add_parser(
        "sell", description="record a sale in sales.csv and exit", help="record a sale in sales.csv and exit")
    # idea: add type=singular to the "product" argument
    parser_sell.add_argument("product", type=lowercase,
                             help="product name - singular noun")
    parser_sell.add_argument("date", type=valid_date,
                             help="sale date - YYYY-MM-DD")
    parser_sell.add_argument("price", type=float,
                             help="sale price - floating point number")
    parser_sell.add_argument("count", type=int, help="product count - integer")
    parser_sell.set_defaults(func=sell)

    # Parse the arguments and call whatever function was selected
    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    main()
