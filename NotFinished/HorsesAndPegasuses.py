from cProfile import run

#from typing import List, Dict, Tuple
#list[int]

class Horse:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
    def run(self):
        print(f'Horse {self.name} running')

class Flyable:
    def __init__(self, speed):
        self.speed = speed

    def fly(self):
        print(f'{self.name} flying with {self.speed} speed')


class Pegasus(Horse, Flyable):
    def __init__(self, color, name, speed):
        Horse.__init__(self, color, name)
        Flyable.__init__(self, speed)
    def run(self):
        print(f'Pegasus {self.name} running')
pegasus = Pegasus('white', 'Mustang', '100km/h')
pegasus.run()
pegasus.fly()
print(pegasus.color, pegasus.name, pegasus.speed)


### about mro() and super()
class Horse:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
    def run(self):
        print(f'Horse {self.name} running')

    def weight(self):
        return 120

class Flyable:
    def __init__(self, speed):
        self.speed = speed

    def fly(self):
        print(f'{self.name} flying with {self.speed} speed')


class Pegasus(Horse, Flyable):
    def __init__(self, color, name, speed):
        Horse.__init__(self, color, name)
        Flyable.__init__(self, speed)

    def run(self):
        print(f'Pegasus {self.name} running')

    def weight(self):
        return super().weight() + 50         ## ошибка вес уже переопределился и появилась рекурсия

pegasus = Pegasus('white', 'Mustang', '100km/h')
#pegasus.run()
#pegasus.fly()
#print(pegasus.color, pegasus.name, pegasus.speed)
#print(Pegasus.mro())
print(pegasus.weight())



### abstractclasses

from abc import ABC, abstractmethod

class Horse:
    def __init__(self, color, name):
        self.color = color
        self.name = name
    
    def run(self):
        print(f'Horse {self.name} running')

    def weight(self):
        return 120

class Flyable(ABC):
    def __init__(self, speed):
        self.speed = speed

    @property
    @abstractmethod 
    def fly (self):
        pass


class Pegasus(Horse, Flyable):
    def __init__(self, color, name, speed):
        Horse.__init__(self, color, name)
        Flyable.__init__(self, speed)

    def run(self):
        print(f'Pegasus {self.name} running')

    def weight(self):
        return super().weight() + 50         ## ошибка вес уже переопределился и появилась рекурсия
    @property
    def fly(self):
        print(f'{self.name} flying with {self.speed} speed')

pegasus = Pegasus('white', 'Mustang', '100km/h')
pegasus.run()
pegasus.fly
#print(pegasus.color, pegasus.name, pegasus.speed)
#print(Pegasus.mro())
print(pegasus.weight())


