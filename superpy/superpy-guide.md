# SuperPy Guide

## Overview

SuperPy is a command-line tool for keeping track of supermarket inventory. It supports recording data from the command-line and displaying data on the command-line. Time is based on the current date.

## Getting Started

1. Open a command-line interface (CLI).
2. Make sure you have Python installed.
3. Go to the directory "superpy".
4. Interact with the program.

## Running the Program

To run the program, enter: `python super.py`.<br>
(Type the name of the programming language after the prompt, followed by the name of the application, then press enter.)

    ➜  superpy ✗ python super.py
    SuperPy running. Please enter a command. For help, enter: 'python super.py -h'.

## Accessing Help

### > General Help

To display general help information, enter `python super.py -h`. Available commands will be displayed on the "usage" line after [-h]. Command descriptions will be displayed under the "positional arguments" line.

    ➜  superpy ✗ python super.py -h
    usage: super.py [-h] {advance,buy,report} ...

    Command-line tool for keeping track of supermarket inventory.

    positional arguments:
    {advance,record,report}
        advance             advance current date
        record              record entered data
        report              report on entered data

    options:
    -h, --help            show this help message and exit

### > Command Help

To display help on a specific command, enter `python super.py <command> -h`. Required arguments will be displayed on the "usage" line after [-h]. Argument descriptions will be displayed under the "positional arguments" line.

    e.g.
    ➜  superpy git:(main) ✗ python super.py advance -h
    usage: super.py advance [-h] days

    Command to advance the current date with a number of days.

    positional arguments:
    days        number of days

    options:
    -h, --help  show this help message and exit

## Executing Commands

There are 3 commands the program can execute: set_date, record and report.

To execute a given command, enter `python super.py <command> <argument(s)>`.

    e.g.
    ➜  superpy ✗ python super.py set_date forwards 10
    ➜  superpy ✗ python super.py record purchase apple 2022-03-01 1.0 2022-03-10 50
    ➜  superpy ✗ python super.py report inventory today

### 1. Set_date

With the "set_date" command the user can set the current date. The "set_date" command requires two arguments: direction and num_days, direction offering "backwards" and "forwards" as choices. Num_days has to be an integer.

On the command-line, enter: `python super.py set_date <direction> <num_days>`

To set date backwards, e.g.:

    ➜  superpy ✗ python super.py set_date backwards 2
    OK
    The current date (2022-03-14) is now set backwards to 2022-03-12.

To set date forwards, e.g.:

    ➜  superpy ✗ python super.py set_date forwards 2
    OK
    The current date (2022-03-14) is now set forwards to 2022-03-16.

There is no limit to the number of days, e.g.: \*

    ➜  superpy ✗ python super.py set_date backwards 100
    OK
    The current date (2022-03-14) is now set backwards to 2021-12-04.

\* Going back to a year BC will throw an OverflowError:

    ➜ superpy ✗ python super.py set_date backwards 1000000
    Traceback (most recent call last):
    File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 86, in <module>
    main()
    File "/Users/saskiaopdam/Desktop/Back-end/superpy/super.py", line 82, in main
    args.func(args)
    File "/Users/saskiaopdam/Desktop/Back-end/superpy/date_setting.py", line 16, in set_date
    adjusted_date = today - timedelta(num_days)
    OverflowError: date value out of range

### 2. Record

With the "record" command the user can record entered data. The "record" command requires one argument: data, which comes in two options: "purchase" and "sale". Both command and argument need to be entered.

    ➜  superpy ✗ python super.py record purchase [purchase arguments]
    ➜  superpy ✗ python super.py record sale [sale arguments]

### > Buy

With the "buy" command the user can record purchase information in a file named bought.csv. The purchase information consists of the product name, purchase date, purchase price, expiration date and number of products.

When entering a future date, a warning is displayed:

    ➜  superpy ✗ python super.py buy cherries 2022-05-01 2.0 2022-03-05 60
    The purchase date (2022-05-01) cannot lay in the future.

When entering a matching product, only the product count is updated:

    ➜  superpy ✗ python super.py buy cherries 2022-03-01 2.0 2022-03-05 60
    OK
    This product matches a previous purchase.
    The number of cherries bought on 2022-03-01 for the price of 2.0 and expiring on 2022-03-05 has been updated from 780 to 840.

When entering a new product, the purchase info is added to the file:

    ➜  superpy git:(main) ✗ python super.py buy passionfruit 2022-03-01 2.0 2022-03-05 60
    OK
    '4334698944 passionfruit 2022-03-01 2.0 2022-03-05 60' has been added to bought.csv.

### > Sell

With the "sell" command the user can record sale information in a file named sold.csv.

### 3. Report

With the "report" command the user can report on recorded data.

- report products (without date)
- report inventory (with date)
- report revenue (with date)
- report profit (with date)

- "command to export selection of data to csv files"
- "commands to execute 2 additional features"

$ python super.py buy --product-name orange --price 0.8 --expiration-date 2020-01-01
OK

$ python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange | 1 | 0.8 | 2020-01-01 |
+--------------+-------+-----------+-----------------+

$ python super.py --advance-time 2
OK

$ python super.py report inventory --yesterday
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+
| Orange | 1 | 0.8 | 2020-01-01 |
+--------------+-------+-----------+-----------------+

$ python super.py sell --product-name orange --price 2
OK

$ python super.py report inventory --now
+--------------+-------+-----------+-----------------+
| Product Name | Count | Buy Price | Expiration Date |
+==============+=======+===========+=================+

$ python super.py report revenue --yesterday
Yesterday's revenue: 0

$ python super.py report revenue --today
Today's revenue so far: 2

$ python super.py report revenue --date 2019-12
Revenue from December 2019: 0

$ python super.py report profit --today
1.2

$ python super.py sell --product-name orange --price 2
ERROR: Product not in stock.
