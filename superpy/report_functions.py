import csv
from date_functions import yesterday, today


def report(args):
    data = args.data
    day = args.day

    def get_date(day):
        if day == "yesterday":
            return yesterday
        elif day == "today":
            return today
    date = get_date(day)
    # if date == "yesterday":
    #     print(data, yesterday)
    # elif date == "today":
    #     print(data, today)
    # elif date == "tomorrow":
    #     print(data, tomorrow)

    def print_heading():
        print(f"{data.capitalize()} {day} ({date}):")
    print_heading()

    def print_data():
        # imlement choice of stdout (terminal or pdf)
        def print_inventory():
            with open('buy.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                row_count = 0
                match_count = 0

                for row in reader:
                    row_count += 1
                    prod_name = row['product_name']
                    count = row['count']
                    buy_price = row['buy_price']
                    exp_date = row['expiration_date']

                    if row['buy_date'] == str(date):
                        match_count += 1
                        print(
                            f"{prod_name}, {count}, {buy_price}, {exp_date}")

                if row_count == 0:
                    print("0 (no products bought so far).")
                if row_count > 0 and match_count == 0:
                    print("0")

        def print_revenue():
            print("revenue data")

        def print_profit():
            print("profit data")

        if data == "inventory":
            print_inventory()
        if data == "revenue":
            print_revenue()
        if data == "profit":
            print_profit()

    print_data()
