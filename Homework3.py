a1 = input('Введите значение 1 катета треугольника ', )
a2 = input('Введите значение 2 катета треугольника ', )
a3 = input('Введите значение 3 катета треугольника ', )
a4 = input('Введите значение 4 катета треугольника ', )

b1 = input('Введите значение 1 катета треугольника ', )
b2 = input('Введите значение 2 катета треугольника ', )
b3 = input('Введите значение 3 катета треугольника ', )
b4 = input('Введите значение 4 катета треугольника ', )

a = [a1, a2, a3, a4]
b = [b1, b2, b3, b4]

#a = input('Введите значение первого катета треугольника ', )
#b = input('Введите значение второго катета треугольника ', )
s = (a*b)/2
c = (a**2+b**2)**0.5
d = {'Катет №1': a, 'Катет №2': b, 'Площадь треугольника': s, 'Гипотинуза': c}
print(d)
