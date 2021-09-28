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

def triang(i, current = 0):
    if current <= i:
        print(str(current) * current)
        return triang(i, current + 1)
    return ''
print(triang(6))
