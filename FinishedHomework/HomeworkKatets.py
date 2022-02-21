


a = [int (i) for i in input().split()]
b = [int (i) for i in input().split()]

for index, (katet1, katet2) in enumerate(zip(a, b), 1):
    
        print(f' Треугольник {index} с катетами {katet1, katet2} имеет площадь {(katet1*katet2)/2}, и гипотинузу {(katet1**2+katet2**2)**0.5}')








