# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите число: '))
a = num
counter_chet = 0
counter_nechet = 0

while num:
    if (num % 10) % 2 == 0:
        counter_chet += 1
    else:
        counter_nechet += 1
    num //= 10
print(f'В числе {a}, {counter_chet} четных(ая) цифр(а) и {counter_nechet} нечетных(ая).')
