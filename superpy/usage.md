# SuperPy - Usage

## Run the program

1. Save SuperPy on your machine.
2. Open a command-line interface (CLI).
3. Make sure you have Python installed.
4. Go to the directory where you saved SuperPy.
5. After the prompt, type 'python super.py' and press Enter:

```
➜  superpy git:(main) ✗ python super.py
usage: python super.py

options:
  -h, --help            show this help message and exit

subcommands:
  {today,yesterday,days_ago,products,stock,revenue,profit,buy,sell}
    today               show today's date and exit
    yesterday           show yesterday's date and exit
    days_ago            show the date n days ago and exit
    products            show the offered products and exit
    stock               show the current stock and exit
    revenue             show the revenue for period x and exit
    profit              show the profit for period x and exit
    buy                 record a purchase in purchases.csv and exit
    sell                record a sale in sales.csv and exit

For subcommand help, enter 'python super.py <subcommand> -h'.
➜  superpy git:(main) ✗
```

## Access help

As you can see in the example above, help is displayed when running the program. Subcommand help can be accessed by entering 'python super.py \<subcommand\> -h'. Any positional (i.e. required) or optional arguments will be displayed in the subcommand help.

**E.g.** get help on "today" subcommand (takes no arguments):

```
➜  superpy git:(main) ✗ python super.py today -h
usage: python super.py today [-h]

show today's date and exit

options:
  -h, --help  show this help message and exit
➜  superpy git:(main) ✗
```

**E.g.** get help on "days_ago" subcommand (takes one positional and one optional argument):

```
➜  superpy git:(main) ✗ python super.py days_ago -h
usage: python super.py days_ago [-h] [-txt] days

show the date n days ago and exit

positional arguments:
  days        number of days

options:
  -h, --help  show this help message and exit
  -txt        export the past date to date.txt
➜  superpy git:(main) ✗
```

**E.g.** get help on "buy" subcommand (takes five positional arguments):

```
➜  superpy git:(main) ✗ python super.py buy -h
usage: python super.py buy [-h] product date price expiration count

record a purchase in purchases.csv and exit

positional arguments:
  product     product name
  date        purchase date - YYYY-MM-DD
  price       purchase price - floating point number
  expiration  expiration date - YYYY-MM-DD
  count       product count - integer

options:
  -h, --help  show this help message and exit
➜  superpy git:(main) ✗
```

## Execute a subcommand

To execute a subcommand, enter 'python super.py \<subcommand\> \[arguments\]'. The program will then call a function with the same name, e.g. today() after "today" has been entered.

### **- today**

Subcommand to show today's date in the terminal.
The function today() prints today's date to the standard output, stdout.
Today() takes no positional or optional arguments.

To execute "today", enter 'python super.py today':

```
➜  superpy git:(main) ✗ python super.py today
2022-03-25
➜  superpy git:(main) ✗
```

### **- yesterday**

Subcommand to show yesterday's date in the terminal.
The function yesterday() prints yesterday's date to the standard output, stdout.
Yesterday() takes no positional or optional arguments.

To execute "yesterday", enter 'python super.py yesterday':

```
➜  superpy git:(main) ✗ python super.py yesterday
2022-03-24
➜  superpy git:(main) ✗
```

### **- days_ago**

Subcommand to show the date n days ago in the terminal.
The function days_ago() prints the date n days ago to the standard output, stdout.
Days_ago() takes one positional argument (days) and one optional argument (-txt).
The optional argument makes the function export the past date to date.txt.

To execute "days_ago", enter: 'python super.py days_ago \<days\>':

```
➜  superpy git:(main) ✗ python super.py days_ago 7
2022-03-18
➜  superpy git:(main) ✗
```

To execute "days_ago" with the option, enter: 'python super.py days_ago \<days\> -txt':

```
➜  superpy git:(main) ✗ python super.py days_ago 7 -txt
2022-03-18 exported to date.txt
➜  superpy git:(main) ✗
```

The past date is now exported to date.txt:

```
2022-03-18
```

You can go back any number of days, e.g.:

```
➜  superpy git:(main) ✗ python super.py days_ago 100
2021-12-15
➜  superpy git:(main) ✗
```

Going back to a year BC will throw an OverflowError:

```
➜  superpy git:(main) ✗ python super.py days_ago 1000000
Traceback (most recent call last):
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 103, in <module>
    main()
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 99, in main
    args.func(args)
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/functions.py", line 23, in days_ago
    past_date = today - timedelta(days_ago)
OverflowError: date value out of range
➜  superpy git:(main) ✗
```

### **-products**

Subcommand to show the offered products in the terminal.
The function products() prints the offered products to the standard output, stdout.
Products() takes one optional argument (-csv).
The optional argument makes the function export the offered products to products.csv.

To execute "products", enter: 'python super.py products':

```
➜  superpy git:(main) ✗ python super.py products
apple
banana
kiwi
➜  superpy git:(main) ✗
```

To execute "products" with the option, enter: 'python super.py products -csv':

```
➜  superpy git:(main) ✗ python super.py products -csv
offered products exported to products.csv
➜  superpy git:(main) ✗
```

The offered products are now exported to products.csv:

```
apple
banana
kiwi
```

### **-stock**

Subcommand to show the current stock in the terminal.
The function stock() prints the current stock to the standard output, stdout.
Stock() takes one optional argument (-csv).
The optional argument makes the function export the current stock to stock.csv.

To execute "stock", enter: 'python super.py stock':

```
➜  superpy git:(main) ✗ python super.py stock
apple: 350
banana: 100
kiwi: 100
➜  superpy git:(main) ✗
```

To execute "stock" with the option, enter: 'python super.py stock -csv':

```
➜  superpy git:(main) ✗ python super.py stock -csv
current stock exported to stock.csv
➜  superpy git:(main) ✗
```

The current stock is now exported to stock.csv:

```
apple,350
banana,100
kiwi,100
```

### **-revenue**

Subcommand to show the revenue for period x in the terminal.
The function revenue() prints the revenue for period x to the standard output, stdout.
Revenue() takes two positional arguments (month and year).

To execute "revenue", enter 'python super.py revenue \<month\> \<year\>':

```
➜  superpy git:(main) ✗ python super.py revenue mar 2022
6.0
➜  superpy git:(main) ✗
```

### **-profit**

Subcommand to show the profit for period x in the terminal.
The function profit() prints the profit for period x to the standard output, stdout.
Profit() takes two positional arguments (month and year).

To execute "profit", enter 'python super.py profit \<month\> \<year\>':

```
➜  superpy git:(main) ✗ python super.py profit mar 2022
5.5
➜  superpy git:(main) ✗
```

### **- buy**

Subcommand to record a purchase in purchases.csv.
The function buy() appends the entered data to this csv file.
Buy() takes five positional arguments: product, date, price, expiration and count.

To execute "buy", enter 'python super.py buy \<product\> \<date\> \<price\> \<expiration\> \<count\>':

```
➜  superpy git:(main) ✗ python super.py buy apple 2022-03-01 1.0 2022-03-10 100
purchase recorded in purchases.csv
➜  superpy git:(main) ✗
```

The purchase data is now appended to purchases.csv:

```
product,date,price,expiration,count
apple,2022-03-01,1.0,2022-03-10,100
```

The "buy" subcommand includes 5 checks:

1. entered dates should have the YYYY-MM-DD format:

```
➜  superpy git:(main) ✗ python super.py buy apple 01-03-2022 1.0 2022-03-10 100
usage: python super.py buy [-h] product date price expiration count
python super.py buy: error: argument date: 01-03-2022 - should be an existing date in the format YYYY-MM-DD.
➜  superpy git:(main) ✗
```

2. entered dates should be existing dates:

```
➜  superpy git:(main) ✗ python super.py buy apple 2022-02-30 1.0 2022-03-10 100
usage: python super.py buy [-h] product date price expiration count
python super.py buy: error: argument date: 2022-02-30 - should be an existing date in the format YYYY-MM-DD.
➜  superpy git:(main) ✗
```

3. the purchase date may not be a future date:

```
➜  superpy git:(main) ✗ python super.py buy apple 2022-06-01 1.0 2022-03-10 100
purchase not recorded - 2022-06-01 is a future date - enter past or current date
➜  superpy git:(main) ✗
```

4. the price should by a floating point number (type=float converts an entered integer to a float)

5. the count should be an integer:

```
➜  superpy git:(main) ✗ python super.py buy apple 2022-03-01 1 2022-03-10 100.0
usage: python super.py buy [-h] product date price expiration count
python super.py buy: error: argument count: invalid int value: '100.0'
➜  superpy git:(main) ✗
```

### **- sell**

Subcommand to record a sale in sales.csv.
The function sell() appends the entered data to this csv file.
Sell() takes four positional arguments: product, date, price and count.

To execute "sell", enter 'python super.py sell \<product\> \<date\> \<price\> \<count\>':

```
➜  superpy git:(main) ✗ python super.py sell apple 2022-03-01 0.5 50
sale recorded in sales.csv
➜  superpy git:(main) ✗
```

The sale data is now appended to sales.csv:

```
product,date,price,count
apple,2022-03-01,0.5,50
```

The "sell" subcommand includes the same 5 checks as the "buy" subcommand (with check 3 applying to the sale date).

It also includes a check on sufficient stock:

```
➜  superpy git:(main) ✗ python super.py sell apple 2022-03-01 0.5 700
sale not recorded - can't sell 700 with 350 on stock
➜  superpy git:(main) ✗
```