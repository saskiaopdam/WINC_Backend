# Imports
import csv

# Variables
from setting_date import today
from products import product_list


def record(args):
    # sub-command function - executes "record" command
    record_purchase = args.data == "purchase"
    record_sale = args.data == "sale"

    if record_purchase:
        print(f"OK\nPurchase data is now recorded.")

    if record_sale:
        print(f"OK\nSale data is now recorded.")


def buy(args):
    product = args.product
    purchase = args.purchase
    price = args.price
    expiration = args.expiration
    count = args.count

    # check if purchase date is realistic
    if purchase > today:
        print(f"The purchase date ({purchase}) cannot lay in the future.")
    else:
        # check if product purchase only needs updating
        rows = []

        def check_need_update():
            need_update = ""
            with open('bought.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # this is the case when the product has already been purchased on the given day for the same price and with the same expiration date
                    if row['product'] == args.product and row['purchase'] == args.purchase.strftime("%Y-%m-%d") and row['price'] == str(args.price) and row['expiration'] == args.expiration.strftime("%Y-%m-%d"):
                        need_update = True
                        # if so, increment the registered count with the entered count
                        updated_count = int(row['count']) + args.count
                        previous_count = int(row['count'])
                        row['count'] = updated_count
                        print(
                            f"OK\nThis product matches a previous purchase.\nThe number of {product} bought on {purchase} for the price of {price} and expiring on {expiration} has been updated from {previous_count} to {updated_count}.")
                    # save all the rows including the updated one to an empty list
                    rows.append(row)

                return need_update

        need_update = check_need_update()

        if need_update:
            def update_purchase():
                # write the rows from the list to the csv file
                with open('bought.csv', 'w', newline="") as csvfile:
                    fieldnames = ['id', 'product', 'purchase',
                                  'price', 'expiration', 'count']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for row in rows:
                        writer.writerow(row)
            update_purchase()

        else:
            def add_purchase():
                # else: add purchase info to the end of buy.csv

                with open('bought.csv', 'a') as csvfile:
                    data = [product, purchase,
                            price, expiration, count]
                    buy_id = id(data)
                    writer = csv.writer(csvfile)
                    writer.writerow([buy_id] + data)
                    print(
                        f"OK\n'{buy_id} {product} {purchase} {price} {expiration} {count}' has been added to bought.csv.")

                # check if purchased product is in product list (i.e. has been bought before)
                if product not in product_list:
                    # if not: add product in product.csv
                    with open('products.csv', 'a') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow({product})
            add_purchase()
