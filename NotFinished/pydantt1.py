from typing import Optional
from pydantic import BaseModel

class Child (BaseModel):
    age : int
    name : str

class Person (BaseModel):
    age : int
    name : str
    children : Optional[list[Child]]
    marries : bool
    city : None

    @property
    def is_above18 (self):
        if self.age >=18:
            return True
        else:
            return False

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

p = Person(**data)
print(p.is_above18)
print(p.children[1])
print(p.json())