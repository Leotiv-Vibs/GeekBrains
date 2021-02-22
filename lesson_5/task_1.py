from collections import namedtuple

# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для
# каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

N = int(input("Введите количество предприятий: "))

Pred = namedtuple('Pred', 'name first second third fourth sum_year')

pred_list = list()
sum_obsh = 0
for i in range(N):
    name = input('Введите название предприятия: ')
    first = int(input('Введите доход за 1 квартал: '))
    second = int(input('Введите доход за 2 квартал: '))
    third = int(input('Введите доход за 3 квартал: '))
    fourth = int(input('Введите доход за 4 квартал: '))

    sum_year = first + second + third + fourth
    sum_obsh += sum_year

    i = Pred(name, first, second, third, fourth, sum_year)

    pred_list.append(i)

sred_prib = sum_obsh / N
less = list()
more = list()
for i in pred_list:
    if i.sum_year > sred_prib:
        more.append(i.name)
    else:
        less.append(i.name)
print("Предприятия чья прибыль за год выше среднего", more)
print("Предприятия чья прибыль за год ниже среднего", less)
