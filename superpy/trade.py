# Imports
import csv

# Sub-command functions


def buy(args):
    with open('buy.csv', 'a') as csvfile:
        data = [args.name, args.buy_date,
                args.price, args.exp_date, args.count]
        buy_id = id(data)
        writer = csv.writer(csvfile)
        writer.writerow([buy_id] + data)

    print(
        f"OK\n'{buy_id} {args.name} {args.buy_date} {args.price} {args.exp_date} {args.count}' now added to buy.csv.")
