# Тесты выполнены на 64-разрядной Win 10 версии 1803
# Python 3.7.2 [MSC v.1916 64 bit (AMD64)] on win32


import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('*'*10)
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if hasattr(var, '__iter__') and not isinstance(var, str):

            if hasattr(var, 'keys'):
                for key, value in var.items():
                    print(f'\nКлюч: \'{key}\' значение {value}')
                    spam += memory_count([key]) + memory_count([value])

            else:
                spam += memory_count(var)

        memory += spam

    return memory


from collections import namedtuple

# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для
# каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

# ****************************************************************
# 1-ЫЙ ВАРИНТ
# *************************************************************
# N = int(input("Введите количество предприятий: "))
#
# Pred = namedtuple('Pred', 'name first second third fourth sum_year')
#
# pred_list = list()
# sum_obsh = 0
# for i in range(N):
#     name = input('Введите название предприятия: ')
#     first = int(input('Введите доход за 1 квартал: '))
#     second = int(input('Введите доход за 2 квартал: '))
#     third = int(input('Введите доход за 3 квартал: '))
#     fourth = int(input('Введите доход за 4 квартал: '))
#
#     sum_year = first + second + third + fourth
#     sum_obsh += sum_year
#
#     i = Pred(name, first, second, third, fourth, sum_year)
#
#     pred_list.append(i)
#
# sred_prib = sum_obsh / N
# less = list()
# more = list()
# for i in pred_list:
#     if i.sum_year > sred_prib:
#         more.append(i.name)
#     else:
#         less.append(i.name)
# # print("Предприятия чья прибыль за год выше среднего", more)
# # print("Предприятия чья прибыль за год ниже среднего", less)
# Затраты памяти программы:  930
# Переменные:  [3, 1, 4, 'i', ['АУЕ', 'ВУК'], ['ОСАГО'], 'ВУК',
# [Pred(name='ОСАГО', first=20, second=30, third=40, fourth=50, sum_year=140),
# Pred(name='АУЕ', first=30, second=10, third=10, fourth=10, sum_year=60),
# Pred(name='ВУК', first=1, second=2, third=3, fourth=4, sum_year=10)],
# 2, 70.0, 210, 10, 3]
# ****************************************************************
# 2-ОЙ ВАРИАНТ
# ******************************************************************
# N = int(input("Введите количество предприятий: "))
#
# # Pred = namedtuple('Pred', 'name first second third fourth sum_year')
#
#
# pred_list = list()
# sum_obsh = 0.0
# for i in range(N):
#     name = input('Введите название предприятия: ')
#     first = float(input('Введите доход за 1 квартал: '))
#     second = float(input('Введите доход за 2 квартал: '))
#     third = float(input('Введите доход за 3 квартал: '))
#     fourth = float(input('Введите доход за 4 квартал: '))
#
#     sum_year = first + second + third + fourth
#
#     i = (name, first, second, third, fourth, sum_year)
#
#     pred_list.append(i)
#
# sred_prib = sum_obsh / N
# less = list()
# more = list()
# for i in pred_list:
#     if i[5] > sred_prib:
#         more.append(i[0])
#     else:
#         less.append(i[0])
# print("Предприятия чья прибыль за год выше среднего", more)
# print("Предприятия чья прибыль за год ниже среднего", less)
# Затраты памяти программы:  836
# Переменные:  [3, 1.0, 4.0, 'i', [], ['qwe', 'asd', 'zxc'], 'zxc',
#               [('qwe', 1.0, 2.0, 3.0, 4.0, 10.0),
#                ('asd', 1.0, 2.0, 3.0, 4.0, 10.0),
#                ('zxc', 1.0, 2.0, 3.0, 4.0, 10.0)], 2.0, 0.0, 0.0, 10.0, 3.0]

# собираем переменные для подсчета затрачиваемой памяти
# ***************************************************************
# 3-ИЙ ВАРИАНТ
# **************************************************************
N = int(input("Введите количество предприятий: "))

# Pred = namedtuple('Pred', 'name first second third fourth sum_year')


pred_list = list()
sum_obsh = 0.0
for i in range(N):
    i = (input('Введите название предприятия: '),
         float(input('Введите доход за 1 квартал: ')),
         float(input('Введите доход за 2 квартал: ')),
         float(input('Введите доход за 3 квартал: ')),
         float(input('Введите доход за 4 квартал: ')))
    sum_obsh += i[1] + i[2] + i[3] + i[4]
    pred_list.append(i)

less = list()
more = list()
for i in pred_list:
    if (i[1] + i[2] + i[3] + i[4]) > sum_obsh / N:
        more.append(i[0])
    else:
        less.append(i[0])
# print("Предприятия чья прибыль за год выше среднего", more)
# print("Предприятия чья прибыль за год ниже среднего", less)
# Затраты памяти программы:  674
# Переменные:  [3, 'i', ['jcfuj', 'qwe'], ['sqwe'], [('jcfuj', 1.0, 2.0, 3.0, 4.0),
# ('qwe', 4.0, 5.0, 6.0, 7.0), ('sqwe', 11.0, 22.0, 33.0, 44.0)], 142.0]
_variable = []
for i in dir():
    if i[0] != '_' and not hasattr(locals()[i], '__name__'):
        _variable.append(locals()[i])

print('\nПеременные: ', _variable, '\n')
print('\nЗатраты памяти программы: ', memory_count(_variable))

# Третий вариант оказался самым
# менее затратным для памяти
# и код стал меньше и переменыых стало меньше, при этом
# уменьшилась чиатабельность, но это не критично в этой ситуации,
# так что третий вариант по праву можно счиатть самым выгодным
