# 6. В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint

random_num = [randint(1, 100) for i in range(10)]

min_value = min(random_num)
max_value = max(random_num)

ind_a = None
ind_i = None

for i, item in enumerate(random_num):
    if item == max_value:
        ind_a = i
    elif item == min_value:
        ind_i = i
print(ind_i, ind_a)
sum = 0
for i, item in enumerate(random_num):
    if ind_i < i < ind_a:
        sum += item
    elif ind_i > i > ind_a:
        sum += item

print(random_num)
print(sum)
