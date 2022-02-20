# def test_example_0():
#     assert 1 == 1


# def test_example_1():
#     assert 1 == 2

def initials(name):
    first, last = name.split(' ')
    f, l = first[0], last[0]
    return f'{f}. {l}.'


def test_initials_common_name():
    assert initials('Daniel Radcliffe') == 'D. R.'


def test_initials_double_barrelled():
    assert initials('Helena Bonham Carter') == 'H. B. C.'
