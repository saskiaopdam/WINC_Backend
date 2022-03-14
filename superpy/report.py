import csv
from date_setting import yesterday, today
from products import product_list


def report(args):
    # data can be: inventory, revenue or profit
    data = args.data
    # day can be: today or yesterday
    day = args.day

    def get_date(day):
        if day == "yesterday":
            return yesterday
        elif day == "today":
            return today
    date = get_date(day)

    def print_heading():
        # E.g. Inventory today (2022-03-10)
        print(f"{data.capitalize()} {day} ({date}):")
    print_heading()

    def print_data():
        # prints inventory, revenue or profit

        def print_inventory():
            products_bought = len(product_list) > 0
            if not products_bought:
                print("No products bought so far, cannot calculate inventory.")
            else:
                for product in product_list:
                    # calculate how many products were bought untill the given day
                    def get_total_purchase_count():
                        total_purchase_count = 0

                        with open('bought.csv') as csvfile:
                            reader = csv.DictReader(csvfile)

                            for row in reader:

                                if row['product'] == product and row['purchase'] <= date.strftime("%Y-%m-%d"):
                                    total_purchase_count += int(row['count'])
                        return total_purchase_count

                    total_purchase_count = get_total_purchase_count()

                    print(
                        f"{product}: {total_purchase_count}")

        def print_products():
            print("products data")
            # alleen "data" argument, geen "date" argument!

        def print_revenue():
            print("revenue data")

        def print_profit():
            print("profit data")
        # imlement choice of stdout (terminal or pdf)
        if data == "products":
            print_products()
        if data == "inventory":
            print_inventory()
        if data == "revenue":
            print_revenue()
        if data == "profit":
            print_profit()

    print_data()
