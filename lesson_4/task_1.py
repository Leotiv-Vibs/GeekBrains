import functools
import cProfile

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 3, 6, 7, 8, 7, 5, 5, 5, 5, 5, 5, 5, 6, 3, 7, 8, 7, 6, 5, 5]


def first(a):
    for i in range(len(a) // 2):
        b = a[i]
        a[i] = a[len(a) - i - 1]
        a[len(a) - i - 1] = b
    return a


cProfile.run('first(a)')
# 1    0.000    0.000    0.000    0.000 task_1.py:8(first)

cProfile.run('first(b)')
# 1    0.000    0.000    0.000    0.000 task_1.py:8(first)


# 1000 loops, best of 5: 1.75 usec per loop first(a)
# 1000 loops, best of 5: 4.33 usec per loop first(b)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def second(array):
    if not array:
        return []
    return [array[-1]] + second(array[:-1])


cProfile.run('second(a)')
# 10/1    0.000    0.000    0.000    0.000 task_1.py:31(second)

cProfile.run('second(b)')
# 26/1    0.000    0.000    0.000    0.000 task_1.py:31(second)

# 1000 loops, best of 5: 4.25 usec per loop second(a)
# 1000 loops, best of 5: 8.59 usec per loop second(b)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = (1, 2, 3, 4, 5, 3, 6, 7, 8, 7, 5, 5, 5, 5, 5, 5, 5, 6, 3, 7, 8, 7, 6, 5, 5)


@functools.lru_cache()
def third(array):
    if not array:
        return []
    return [array[-1]] + third(array[:-1])


cProfile.run('third(a)')
# 10/1    0.000    0.000    0.000    0.000 task_1.py:51(third)

cProfile.run('third(b)')
# 20/1    0.000    0.000    0.000    0.000 task_1.py:51(third)

# 1000 loops, best of 5: 205 nsec per loop third(a)
# 1000 loops, best of 5: 244 nsec per loop third(b)


# Лучшим вариантом оказался рекурсивный метод с использованием итератора 'lru_cache'
# он работает быстрее чем остальные вариант.
