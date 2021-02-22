# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

random_num = [randint(1, 100) for i in range(21)]

min_value = min(random_num)
max_value = max(random_num)
print(max_value, min_value)

ind_a = None
ind_i = None
print(random_num)
for i, item in enumerate(random_num):
    if item == max_value and ind_a == None:
        ind_a = i

    elif item == min_value and ind_i == None:
        ind_i = i
random_num[ind_i], random_num[ind_a] = random_num[ind_a], random_num[ind_i]
print(ind_i, ind_a)
print(random_num)
