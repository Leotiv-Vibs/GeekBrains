# Отсортируйте по возрастанию методом
# слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random

array = [random.randint(-100, 100) for i in range(200)]
print('Изначальный массив: ', array)


def merge(left, right):
    result_ = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result_.append(left[i])
            i += 1
        else:
            result_.append(right[j])
            j += 1
    result_ += left[i:] + right[j:]
    return result_


def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left = array[:len(array) // 2]
        right = array[len(array) // 2:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort(array))
