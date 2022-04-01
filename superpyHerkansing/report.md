# SuperPy - Report

## Three technical aspects worth mentioning

### 1. Subparsers:

The program needs to do different things based on different command-line inputs. One out-of-the box way to achieve this is by using the .add_subparsers() method from the argparse module. Argparse is part of the python standard library. It is the best solution I have found so far, although the Click module might also do the trick.

### 2. File formats:

The subcommands "products" and "stock" can potientally print substiantial amounts of data to the standard output. The user might want to export those data to another file for further processing. As csv and excel are two widely used fileformats to process data, I decided to add export options for csv and excel to both subcommands.

## 3. Tables:

The subcommands "products" and "stock" can potientally print substiantial amounts of data to the standard output. To improve on readability, I chose to present the data in tabular format by using the module beautifultable. There are multiple python modules that serve the same purpose, I simply liked the dotted style provided in beautifultable.
