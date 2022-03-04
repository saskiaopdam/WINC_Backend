# 3 technical notes

## 1. Subparsers:

Use of subparsers to read and handle different commands with their associated arguments. This allows the programme to do different things depending on the set of arguments entered by the user on the command line. As far as I could find, the only way to achieve this is by using the .add_subparsers() method provided in the argparse module.

Argument set:

- `python super.py <command> <argument(s)>`

E.g.

- `python super.py advance 2` (advance with 2 days)

Available choices:

- 'advance' + argument: days
- 'buy' + arguments: name, date, price, exp, count
- 'report' + arguments: result, date
