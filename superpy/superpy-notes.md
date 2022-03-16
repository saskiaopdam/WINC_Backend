# SuperPy Notes

## 1. Subparsers and decorators:

The program needs to do different things based on different command-line inputs. One out-of-the box way to achieve this is by using the .add_subparsers() method from the argparse module. Argparse is part of the python standard library.

Argparse code tends to be rather verbose. To shorten the code and improve it's readability, decorators prove to come in handy. For documentation, see Mike Depalatis's blog [Simplifying argparse usage with subcommands](https://mike.depalatis.net/blog/simplifying-argparse.html).

Both solutions are the best I have found so far, although the Click module might also do the trick.
