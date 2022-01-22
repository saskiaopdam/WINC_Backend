example_names = ['Anna Ansville', 'Bob Bobsville', 'Carla Carsville']
example_last_names = [n.split(' ')[-1] for n in example_names]
print(example_last_names)

squares = []
for i in range(10):
    squares.append(i * i)
    
squares = [i * i for i in range(10)]

print(squares)

sentence = "the rocket came back from mars"
vowels = [i for i in sentence if i in "aeiou"]
print(vowels)