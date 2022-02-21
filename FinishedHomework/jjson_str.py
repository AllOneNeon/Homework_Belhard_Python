import json

class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    
    def __str__(self):
        return (f'Это точка с координатами {self.x} и {self.y}')

x = '11'
y = '22'

xd = json.dumps(x)
yd = json.dumps(y)

x1 = json.loads(xd)
x2 = json.loads(yd)

pt1 = Point(x1, x2)
print(str(pt1))