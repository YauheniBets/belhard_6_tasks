"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""
numbers_list = []
def sum_of_numbers(n):
    if (n == 0):
        return numbers_list
    dig = n % 10
    numbers_list.append(dig)
    sum_of_numbers(n // 10)
sum_of_numbers(11)
print(sum(numbers_list))