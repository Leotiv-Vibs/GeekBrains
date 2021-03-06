# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например,
# если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.


from random import random

print("Введите два целых числа и вы получите рандомное число в этом диапозоне, ввод начинать с меньшего числа")
a = int(input("Введите целое число начала интервала: "))
b = int(input("Введите целое число конца интервала: "))
n = int(random() * (b - a + 1)) + a
print(f"Рандомное целое число в интервале {a} - {b} : {n}")

print("Введите два вещественных числа и вы получите рандомное число в этом диапозоне, ввод начинать с меньшего числа")
a = float(input("Введите вещественное число начала интервала: "))
b = float(input("Введите вещественное число начала интервала: "))
n = random() * (b - a) + a
print(f"Рандомное вещественное число в интервале {a} - {b} : {round(n, 2)}")

print("Введите два символа алфавита и вы получите рандомный символ в этом диапозоне, ввод начинать с ранней буквы")
a = ord(input("Введите символ начала интервала: "))
b = ord(input("Введите символ начала интервала: "))
n = int(random() * (b - a + 1)) + a
print(f"Рандомный символ в интервале {chr(a)} - {chr(b)} : {chr(n)}")
