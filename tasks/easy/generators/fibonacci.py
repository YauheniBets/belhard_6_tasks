"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""
def fibonacci(end_number):
    a, b = 1, 1
    for i in range(end_number):
        yield a
        a, b = b, a + b
for i in fibonacci(100):
    print(i)