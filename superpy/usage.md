# SuperPy - Usage

## Run the program

1. save SuperPy on your machine.
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
  {today,yesterday,days_ago,buy}
    today               show today's date and exit
    yesterday           show yesterday's date and exit
    days_ago            show the date n days ago and exit
    buy                 record a purchase in purchases.csv and exit

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
  -txt        export the past date to past_date.txt
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
2022-03-24
➜  superpy git:(main) ✗
```

### **- yesterday**

Subcommand to show yesterday's date in the terminal.
The function yesterday() prints yesterday's date to the standard output, stdout.
Yesterday() takes no positional or optional arguments.

To execute "yesterday", enter 'python super.py yesterday':

```
➜  superpy git:(main) ✗ python super.py yesterday
2022-03-23
➜  superpy git:(main) ✗
```

### **- days_ago**

Subcommand to show the date n days ago in the terminal.
The function days_ago() prints the date n days ago to the standard output, stdout.
Days_ago() takes one positional argument (days) and one optional argument (-txt).
The optional argument makes the function export the past date to past_date.txt.

To execute "days_ago", enter: 'python super.py days_ago \<days\>':

```
➜  superpy git:(main) ✗ python super.py days_ago 7
2022-03-17
➜  superpy git:(main) ✗
```

To execute "days_ago" with the option, enter: 'python super.py days_ago \<days\> -txt':

```
➜  superpy git:(main) ✗ python super.py days_ago 7 -txt
2022-03-17 exported to date.txt
➜  superpy git:(main) ✗
```

The past date is now exported to date.txt:

```
2022-03-17
```

You can go back any number of days, e.g.:

```
➜  superpy git:(main) ✗ python super.py days_ago 100
2021-12-14
➜  superpy git:(main) ✗
```

Going back to a year BC will throw an OverflowError:

```
➜  superpy git:(main) ✗ python super.py days_ago 1000000
Traceback (most recent call last):
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 53, in <module>
    main()
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 49, in main
    args.func(args)
  File "/Users/saskiaopdam/Desktop/Back-end/superpy/functions.py", line 20, in days_ago
    past_date = today - timedelta(days_ago)
OverflowError: date value out of range
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

The function buy() includes 3 checks:

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
purchase not recorded - the purchase date may not be a future date
➜  superpy git:(main) ✗
```
