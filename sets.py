# x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
# x = {'foo', 'bar', 'baz', 'foo', 'qux'}
# # x = ['foo', 'bar', 'baz', 'foo', 'qux']
# print(x) # {'foo', 'bar', 'baz', 'qux'}

# x = set(('foo', 'bar', 'baz', 'foo', 'qux'))
# # x = ('foo', 'bar', 'baz', 'foo', 'qux')
# print(x) # {'foo', 'bar', 'baz', 'qux'}

# s = 'quux'
# set(s)
# print(set(s)) # {'q','u','x'}
# print(list(s)) # ['q','u','u','x']

# x = {'q', 'u', 'u', 'x'}
# print(x) # {'q', 'u', 'x'}

# x = {'foo'}
# print(x) # {'foo}

# x = set('foo')
# print(x) # {'f', 'o'}
# print(len(x)) # 2
# print('f' in x)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1 | x2) # {'foo', 'bar', 'baz', 'qux', 'quux'}
print(x1.union(x2))
print(x1 & x2) # {'baz'}
print(x1.intersection(x2)) # {'baz'}
a = {1,2,3,30,300}
b = {10,20,30,40}
c = {100,200,300,400}
print(a.difference(b,c)) # {1,2,3}
print(a - b - c) # {1,2,3}