from main import get_none, flatten_dict, flatten_dict_complete


def test_get_none():
    assert get_none() == None


# def test_flatten_dict():
#     assert flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]
#     assert flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]
#     assert flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [
#         {'inner_a': 42, 'inner_b': 350}, 3.14]
#     assert flatten_dict({'a': [{'inner_inner_a': 42}]}) == [[
#         {'inner_inner_a': 42}]]


def test_flatten_dict_complete():
    list = []
    # 1
    # assert flatten_dict_complete({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}, list) == [
    #     42, 350, 3.14]

    # 2
    # assert flatten_dict_complete({'a': {'inner_a': 42, 'inner_b': {
    #     'inner_y': 60, 'inner_z': 70}}, 'b': [3.14, 150], 'c': 40}, list) == [
    #     42, 60, 70, [3.14, 150], 40]

    # 3
    # assert flatten_dict_complete({'a': {'inner_a': 42, 'inner_b': {'inner_a': 100, 'inner_b': 400}}, 'b': 3.14}, list) == [
    #     42, 100, 400, 3.14]

    # 4
    assert flatten_dict_complete({'a': [{'inner_inner_a': 42}]}, list) == [42]
