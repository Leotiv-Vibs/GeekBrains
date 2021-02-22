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