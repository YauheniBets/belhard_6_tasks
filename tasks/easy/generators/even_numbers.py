"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""
def get_even_number(i):
    for even in range(i):
        if even % 2 == 0:
            yield even



for i in get_even_number(100):
    print(i)