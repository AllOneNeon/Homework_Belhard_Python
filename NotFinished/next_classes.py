class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
        self.full = f'{fn} {ln}' #ошибка!!!
    
p = Person('Alex', 'Schmidt')
p.ln = 'sidorov'
print(p.full)

###
class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
    def get_fullname(self):
        return f'{self.fn} {self.ln}'
    def set_fullname(self, fullname):
        self.fn, self.ln = fullname.split('')
p = Person('Alex', 'Schmidt')
p.ln = 'sidorov'
print(p.get_fullname())

###
class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln
    def get_fullname(self):
        return f'{self.fn} {self.ln}'

    def set_fullname(self, fullname):
        data = fullname.split(' ')
        if len(data) != 2:
            raise ValueError
        self.fn, self.ln = data

p = Person('Alex', 'Schmidt')
print(p.get_fullname())
p.set_fullname ('Артем Иванов')
print(p.get_fullname())
print(p.fn)
print(p.ln)

###
class Person:
    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    @property
    def fullname(self):
        return f'{self.fn} {self.ln}'

    @fullname.setter
    def fullname(self, fullname):
        data = fullname.split(' ')
        if len(data) != 2:
            raise ValueError ('must be 2 lexems instead of {len(data)}')
        self.fn, self.ln = data

p = Person('Alex', 'Schmidt')
print(p.fullname)
p.fullname = 'Artem Ivanov'
print(p.fullname)
print(p.fn)
print(p.ln)