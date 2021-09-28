"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular(i, current=0):
    if current <= i:
        print(str(current) * current)
        return triangular(i, current + 1)
    return str(current) * current


print(triangular(6))
