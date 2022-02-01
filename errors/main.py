# Do not modify these lines
import os

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"
__human_name__ = "errors"


# Test your functions here to make sure the functionality remains the same.
def main():
    foo = list(range(10))
    print(
        get_item_from_list(foo, 9),
        get_item_from_list(foo, -1),
        get_item_from_list(foo, 10),
    )
    ...

    print(add("1", 1))
    print(read_file("boem.py"))
    print(get_item_from_list(["jan", "feb", "mrt"], 5))


"""Change the three functions below from Look Before You Leap (LBYL) to Easier
to Ask for Forgiveness than Permission (EAFP)"""


# Returns the addition of x and y if it's defined, otherwise returns 0
def add(x, y):
    try:
        return x + y
    except TypeError:
        return 0
    
# Returns the contents of the file at 'filename', or an empty string if the
# file does not exist
def read_file(filename):
    # if os.path.exists(filename):
    #     return open(filename, "r").read()
    # else:
    #     return ""
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        return ""


# Returns item at `index` from list `l` if possible, otherwise returns None
def get_item_from_list(l, index):
    # max_index = len(l) - 1
    # min_index = -1 - max_index
    # if index <= max_index and index >= min_index:
    #     return l[index]
    # else:
    #     return None
    try:
        return l[index]
    except IndexError:
        return None


if __name__ == "__main__":
    main()
