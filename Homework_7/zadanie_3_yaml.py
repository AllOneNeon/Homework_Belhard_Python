import yaml


names_yaml = 'Eric, Justin, Dan'

names = yaml.safe_load(names_yaml)
print (names)

names = yaml.dump (names_yaml)
print (names)



data = {
    'age': 45,
    'name': 'Peter',  
    }


with open ('dump', 'w') as f:
    yaml.dump (data, f)
    print (data)

with open ('dump', 'r') as f:
    data = yaml.safe_load (f)
    print (data)