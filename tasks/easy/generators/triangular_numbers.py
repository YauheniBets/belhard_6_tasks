"""
Написать генератор triangular_numbers, который возвращает подряд числа
треугольные числа


Формула:
Tn = 1 / 2 * n * (n + 1)


Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""
def triangular_numbers(end_number):

    tn = int(1 / (2 * end_number * (end_number + 1)))
    for i in range(1, end_number):
        yield tn
        tn += i

for i in triangular_numbers(10):
    print(i)