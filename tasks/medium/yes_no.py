"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

a = input('Введите числа через пробел: ').split()
def yes_or_no(a):
    for i in range(len(a)):
        if a[i] in a[:i]:
            print ('YES')
        else:
            print ('NO')
yes_or_no(a)