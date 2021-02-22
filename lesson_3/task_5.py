# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
a = [1, 2, 3, 4, 5, 5, -10, -1, -2000]
max_ = 0
ind = 0
for i, item in enumerate(a):
    if item < 0 and max_ == 0:
        max_, ind = item, i
    elif 0 > item > max_:
        max_, ind = item, i
print(max_, ind)
