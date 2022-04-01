# SuperPy - Usage

## Run the program

1. Save SuperPy on your machine.
2. Open a command-line interface (CLI).
3. Make sure you have Python installed.
4. Install the Python modules XlsxWriter and beautifultable.
5. Go to the directory where you saved SuperPy.
6. After the prompt, type 'python super.py' and press Enter:

```
➜  superpy git:(main) ✗ python super.py
usage: python super.py

options:
  -h, --help            show this help message and exit

subcommands:
  {today,yesterday,advance_today,products,stock,revenue,profit,buy,sell}
    today               show today's date and exit
    yesterday           show yesterday's date and exit
    advance_today       advance 'today' with n days and exit
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

**E.g.** get help on "products" subcommand (takes two optional arguments):

```
➜  superpy git:(main) ✗ python super.py products -h
usage: python super.py products [-h] [-csv] [-excel]

show the offered products and exit

options:
  -h, --help  show this help message and exit
  -csv        export the offered products to products.csv
  -excel      export the offered products to products.xlsx
➜  superpy git:(main) ✗
```

**E.g.** get help on "buy" subcommand (takes five positional arguments):

```
➜  superpy git:(main) ✗ python super.py buy -h
usage: python super.py buy [-h] product date price expiration count

record a purchase in purchases.csv and exit

positional arguments:
  product     product name - singular noun
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
Today's date is the date recorded in the text file "today.txt".
Today() takes no positional or optional arguments.

To execute "today", enter 'python super.py today'.

If no date has been recorded in "today.txt", the current date is printed:

```
➜  superpy git:(main) ✗ python super.py today
Today: 2022-04-01
➜  superpy git:(main) ✗
```

If today has been advanced by a number of days using the "advance_today" subcommand described below, the advanced date is printed:

```
➜  superpy git:(main) ✗ python super.py today
Today: 2022-03-30
➜  superpy git:(main) ✗
```

### **- yesterday**

Subcommand to show yesterday's date in the terminal.
The function yesterday() prints yesterday's date to the standard output, stdout.
Yesterday's date is calculated relative to the date recorded in the text file "today.txt" as today's date.
Yesterday() takes no positional or optional arguments.

To execute "yesterday", enter 'python super.py yesterday':

```
➜  superpy git:(main) ✗ python super.py yesterday
Yesterday: 2022-03-29
➜  superpy git:(main) ✗
```

### **- advance_today**

Subcommand to advance 'today' with n days.
The function advance_today() advances today's date - as recorded in today.txt - with n days.
Advance_today() takes one positional argument (days).

To execute "advance_today", enter: 'python super.py advance_today \<days\>':

```
➜  superpy git:(main) ✗ python super.py advance_today 2
Today is advanced with 2 days from 2022-04-01 to 2022-03-30.
➜  superpy git:(main) ✗
```

The 'new today' is recorded in today.txt:

```
2022-03-30
```

You can go back any number of days, e.g.:

```
➜  superpy git:(main) ✗ python super.py advance_today 100
Today is advanced with 100 days from 2022-03-30 to 2021-12-20.
➜  superpy git:(main) ✗
```

Going back to a year BC will throw an OverflowError:

```
➜  superpy git:(main) ✗ python super.py advance_today 738395
Traceback (most recent call last):
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 115, in <module>
    main()
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 111, in main
    args.func(args)
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/functions.py", line 57, in advance_today
    new_today = today - timedelta(days)
OverflowError: date value out of range
➜  superpy git:(main) ✗
```

### **-products**

Subcommand to show the offered products in the terminal.
The function products() prints the offered products to the standard output, stdout.
Products() takes two optional arguments (-csv and -excel).
The optional arguments make the function export the offered products to either products.csv or products.xlsx.

To execute "products", enter: 'python super.py products':

```
➜ superpy git:(main) ✗ python super.py products
...........
: product :
...........
: apple :
: banana :
: kiwi :
: mango :
...........
➜ superpy git:(main) ✗
```

To execute "products" with the option -csv, enter: 'python super.py products -csv':

```
➜ superpy git:(main) ✗ python super.py products -csv
offered products exported to products.csv
➜ superpy git:(main) ✗
```

The offered products are now exported to products.csv:

```
product
apple
banana
kiwi
mango
```

To execute "products" with the option -excel, enter: 'python super.py products -excel':

```
➜ superpy git:(main) ✗ python super.py products -excel
offered products exported to products.xlsx
➜ superpy git:(main) ✗
```

Open the file products.xlsx in Excel to see the result.

### **-stock**

Subcommand to show the current stock in the terminal.
The function stock() prints the current stock to the standard output, stdout.
The current stock is the stock on today's date as recorded in today.txt.
Stock() takes two optional arguments (-csv and -excel).
The optional arguments make the function export the current stock to either stock.csv or stock.xlsx.

To execute "stock", enter: 'python super.py stock':

```
➜  superpy git:(main) ✗ python super.py stock
Stock today (2022-03-30):
.......................
: product :     stock :
.......................
: apple   :       350 :
: banana  :       250 :
: kiwi    :       100 :
: mango   :         0 :
.......................
➜  superpy git:(main) ✗
```

To execute "stock" with the option -csv, enter: 'python super.py stock -csv':

```
➜ superpy git:(main) ✗ python super.py stock -csv
current stock exported to stock.csv
➜ superpy git:(main) ✗
```

The current stock is now exported to stock.csv:

```
product,stock
apple,350
banana,250
kiwi,100
mango,0
```

To execute "stock" with the option -excel, enter: 'python super.py stock -excel':

```
➜ superpy git:(main) ✗ python super.py stock -excel
current stock exported to stock.xlsx
➜ superpy git:(main) ✗
```

Open the file stock.xlsx in Excel to see the result.

### **-revenue**

Subcommand to show the revenue for period x in the terminal.
The function revenue() prints the revenue for period x to the standard output, stdout.
Revenue() takes three optional arguments (-today, -yesterday and -month).

To execute "revenue", enter 'python super.py revenue \[option]'.

If you execute "revenue" without an option, the program will prompt you to add one:

```
➜ superpy git:(main) ✗ python super.py revenue
please enter an option - see 'python super.py revenue -h'
➜ superpy git:(main) ✗
```

With the option "-today":

('Today' is today's date as recorded in today.txt.)

```
➜  superpy git:(main) ✗ python super.py revenue -today
Revenue today (2022-03-30):
0
➜  superpy git:(main) ✗
```

With the option "-yesterday":

```
➜  superpy git:(main) ✗ python super.py revenue -yesterday
Revenue yesterday (2022-03-29):
0
➜  superpy git:(main) ✗
```

With the option "-month":

```
➜ superpy git:(main) ✗ python super.py revenue -month mar-2022
Revenue March 2022:
50.0
➜ superpy git:(main) ✗
```

### **-profit**

Subcommand to show the profit for period x in the terminal.
The function profit() prints the profit for period x to the standard output, stdout.
Profit() takes three optional arguments (-today, -yesterday and -month).

To execute "profit", enter 'python super.py profit \[option]'.

If you execute "profit" without an option, the program will prompt you to add one:

```
➜ superpy git:(main) ✗ python super.py profit
please enter an option - see 'python super.py profit -h'
➜ superpy git:(main) ✗
```

With the option "-today":

('Today' is today's date as recorded in today.txt.)

**E.g.** with today == 2022-03-28:

```
➜  superpy git:(main) ✗ python super.py profit -today
Profit today (2022-03-28):
-450.0
➜  superpy git:(main) ✗
```

With the option "-yesterday":

```
➜  superpy git:(main) ✗ python super.py profit -yesterday
Profit yesterday (2022-03-27):
0
➜  superpy git:(main) ✗
```

With the option "-month":

```
➜  superpy git:(main) ✗ python super.py profit -month mar-2022
Profit March 2022:
-1050.0
➜  superpy git:(main) ✗
```

### **- buy**

Subcommand to record a purchase in purchases.csv.
The function buy() appends the entered data to this csv file.
Buy() takes five positional arguments: product, date, price, expiration and count.

To execute "buy", enter 'python super.py buy \<product\> \<date\> \<price\> \<expiration\> \<count\>':

```
➜ superpy git:(main) ✗ python super.py buy apple 2022-03-01 1.0 2022-03-10 100
purchase recorded in purchases.csv
➜ superpy git:(main) ✗
```

The purchase data is now appended to purchases.csv:

```
product,date,price,expiration,count
apple,2022-03-01,1.0,2022-03-10,100
```

The "buy" subcommand includes 7 checks:

1. the product name should be lowercase (the type keyword for the argument "product" (type=lowercase) converts a string to lowercase)

2. entered dates should have the YYYY-MM-DD format:

```
➜ superpy git:(main) ✗ python super.py buy apple 01-03-2022 1.0 2022-03-10 100
usage: python super.py buy [-h] product date price expiration count
python super.py buy: error: argument date: 01-03-2022 - should be an existing date in the format YYYY-MM-DD
➜ superpy git:(main) ✗
```

3. entered dates should be existing dates:

```
➜ superpy git:(main) ✗ python super.py buy apple 2022-02-30 1.0 2022-03-10 100
usage: python super.py buy [-h] product date price expiration count
python super.py buy: error: argument date: 2022-02-30 - should be an existing date in the format YYYY-MM-DD
➜ superpy git:(main) ✗
```

4. the purchase date may not be a future date:

```
➜ superpy git:(main) ✗ python super.py buy apple 2022-06-01 1.0 2022-03-10 100
purchase not recorded - 2022-06-01 is a future date - please enter past or current date
➜ superpy git:(main) ✗
```

5. the expiration date should be a future date:

```
➜  superpy git:(main) ✗ python super.py buy banana 2022-03-28 2.0 2022-03-10 100
purchase not recorded - 2022-03-28 is a past or current date - please enter a future date
➜  superpy git:(main) ✗
```

6. the price should by a floating point number (the type keyword for the argument "price" (type=float) converts an entered integer to a float)

7. the count should be an integer:

```
➜ superpy git:(main) ✗ python super.py buy apple 2022-03-01 1 2022-03-10 100.0
usage: python super.py buy [-h] product date price expiration count
python super.py buy: error: argument count: invalid int value: '100.0'
➜ superpy git:(main) ✗
```

**Idea:** Add type=singular to the "product" argument

It would be a good idea to add a type conversion for the product name to prevent doubles like "banana" and "banana's" ending up in the product list. For more details see the docstring in functions.py at def singular().

### **- sell**

Subcommand to record a sale in sales.csv.
The function sell() appends the entered data to this csv file.
Sell() takes four positional arguments: product, date, price and count.

To execute "sell", enter 'python super.py sell \<product\> \<date\> \<price\> \<count\>':

```
➜ superpy git:(main) ✗ python super.py sell banana 2022-03-01 0.5 50
sale recorded in sales.csv
➜ superpy git:(main) ✗
```

The sale data is now appended to sales.csv:

```
product,date,price,count
apple,2022-03-27,0.5,50
banana,2022-03-01,0.5,50
```

The "sell" subcommand includes the same 7 checks as the "buy" subcommand (with check 4 applying to the sale date), except the check on expiration date.

It also includes a check on sufficient stock:

```
➜ superpy git:(main) ✗ python super.py sell apple 2022-03-01 0.5 50
Apple in stock on 2022-03-01: 0.
Sale not recorded - can't sell 50 with 0 in stock.
➜ superpy git:(main) ✗
```

**Idea:** Add type=singular to the "product" argument

It would be a good idea to add a type conversion for the product name to prevent doubles like "banana" and "banana's" ending up in the product list. For more details see the docstring in functions.py at def singular().
