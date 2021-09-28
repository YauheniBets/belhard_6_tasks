"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""

def factorial(n: int) -> int:
    count = 1
    for i in range(1, n + 1):
        count *= i
        yield count

for i in factorial(6):
    print(i)
