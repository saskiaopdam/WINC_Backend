import csv

from date_functions import today
from products import product_list


def buy(args):
    product_name = args.name
    buy_date = args.buy_date
    price = args.price
    exp_date = args.exp_date
    count = args.count

    # check if purchase date is realistic
    if buy_date > today:
        print(f"The buy_date ({buy_date}) cannot lay in the future.")
    else:
        # add purchase info to buy.csv
        with open('buy.csv', 'a') as csvfile:
            data = [product_name, buy_date,
                    price, exp_date, count]
            buy_id = id(data)
            writer = csv.writer(csvfile)
            writer.writerow([buy_id] + data)
            print(
                f"OK\n'{buy_id} {product_name} {buy_date} {price} {exp_date} {count}' has been added to buy.csv.")

        # check if purchased product is in product list
        print(product_list)
        if product_name not in product_list:
            # record product in product.csv
            with open('products.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow({product_name})
