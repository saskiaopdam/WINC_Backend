import csv


def get_product_list():
    product_list = []
    with open('products.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            product = row['product']
            if product not in product_list:
                product_list.append(product)
    return product_list


product_list = get_product_list()
