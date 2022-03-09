import csv


def get_product_list():
    product_list = []
    with open('products.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            product_name = row['product_name']
            if product_name not in product_list:
                product_list.append(product_name)
    return product_list


product_list = get_product_list()
