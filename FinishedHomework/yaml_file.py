import yaml

data = {
    'age' : 35,
    'name' : 'John',
    'children':
    [
        {
            'age': 5,
            'name': 'Mia'},
        {
            'age': 9,
            'name': 'Kyle'}
    ],
    'married': True,
    'city': None}

with open ('data.yaml', 'w') as file:
    yaml.dump(data, file)
with open ('data.yaml') as file:
    data1 = yaml.safe_load(file)
print(data1)

child = data1.get('age')
print(child)