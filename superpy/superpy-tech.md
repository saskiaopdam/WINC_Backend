# SuperPy

## Technical notes

### 1. Subparsers:

- description:
  .add_subparsers() method from the argparse module - allows for reading and handling different commands with their associated arguments on the command line

- problem solved:
  performing different actions based on different commands entered by user on the command line according to the scheme `python super.py <command> <argument(s)>` - where command can be advance, buy, sell or report. E.g. `python super.py advance 2` leading to the action advance with 2 days.

- reason to implement:
  out-of-the box solution provided in python standard library (Click module could be a possible alternative)
