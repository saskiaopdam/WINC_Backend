import pytest


def get_none():
    return None


def flatten_dict(dict):
    return(list(dict.values()))


def flatten_dict_complete(dictionary, flattend):
    for value in dictionary.values():
        if type(value) is dict:
            print("value is a dictionary")
            flatten_dict_complete(value, flattend)
        elif type(value) is list:
            for x in value:
                if type(x) is dict:
                    return flatten_dict_complete(x, flattend)
            flattend.append(value)
        else:
            flattend.append(value)
    return flattend


flattend = []

# 1
# dictionary = {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}

# 2
# dictionary = {'a': {'inner_a': 42, 'inner_b': {
#     'inner_y': 60, 'inner_z': 70}}, 'b': [3.14, 150], 'c': 40}

# 3
# dictionary = {'a': {'inner_a': 42, 'inner_b': {
#     'inner_a': 100, 'inner_b': 400}}, 'b': 3.14}

# 4
dictionary = {'a': [{'inner_inner_a': 42}]}

print(flatten_dict_complete(
    dictionary, flattend))


# iterate


def iteratively_solve_some_problem(n):
    for i in range(1, n + 1):
        print(f"case {i}")


# recursion
basecase = 1


def recursively_solve_some_problem(n):
    if n == basecase:
        print("basecase")
        return
    elif n > basecase:
        print(f"case {n}")
        return recursively_solve_some_problem(n - 1)


# iteratively_solve_some_problem(1)
# recursively_solve_some_problem(5)


# print(flatten_dict_complete(
#     {'a': {'inner_a': 42, 'inner_b': {'inner_a': 100, 'inner_b': 400}}, 'b': 3.14}))
# # [42, {'inner_a': 100, 'inner_b': 400}, 3.14]

# print(flatten_dict_complete({'a': [{'inner_inner_a': 42}]}))
# # [[{'inner_inner_a': 42}]]
