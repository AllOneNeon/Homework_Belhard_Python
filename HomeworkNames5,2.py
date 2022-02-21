persons = [{'Name': 'Anna', 'Age': 17, 'Sex': 'Female'}, 
    {'Name': 'Andrew', 'Age': 26, 'Sex': 'Male'}]

num_people = []
for i in persons:
    num_people.append(i['Name'])
print('Количество людей: ' , len(num_people))

num_male = [xy for xy in persons if xy['Sex'] == 'Male']
print('Количество мужчин: ' , len(num_male))

num_female = [xx for xx in persons if xx['Sex'] == 'Female']
print('Количество женщин: ' , len(num_female))

num_of_legal_age = [d for d in persons if d['Age'] >= 18]
print('Количество совершеннолетних людей: ' , len(num_of_legal_age))

num_name = []
for n in persons:
    num_name.append(n['Name'])
print('использованые имена: ' , num_name)

num_age = []
for a in persons:
    num_age.append(a['Age'])
    num_age.sort()
print('Список возрастов: ' , num_age)

from collections import Counter
num_commons = []
for c in persons:
    num_commons.append(c['Name'])
print('3 самых часто встречающихся имени: ' , [element for element, count in Counter(num_commons).most_common(3)])
male_names = [mn for mn in persons if mn['Sex'] == 'Male' and mn['Age'] > 25 and mn['Name'][0] == 'A']
names = [mn['Name'] for mn in male_names]
print('Имена мужчин старше 35 лет, чье имя начинается с буквы A: ' , names)