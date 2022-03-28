# SuperPy - Report

## Three technical aspects worth mentioning

1. Subparsers:

The program needs to do different things based on different command-line inputs. One out-of-the box way to achieve this is by using the .add_subparsers() method from the argparse module. Argparse is part of the python standard library. It is the best solution I have found so far, although the Click module might also do the trick.

2. File formats:

- Option to export to csv or excel

The subcommands "products" and "stock" offer two options to export the stock data to a file other than the standard output. The user can choose to export to csv or to excel by entering either -csv or -excel after the subcommand. If no option is chosen, de products or stock gets printed to the terminal.

```
Mention 3 technical plusses:

- description
- which problem they solve
- why you chose this implementation

- code snippets allowed for illustration
```
