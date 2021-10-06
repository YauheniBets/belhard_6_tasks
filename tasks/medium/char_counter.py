"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def counts_char(STR_VAL:str) -> dict:
    counts_dict = {}
    for char in list(STR_VAL):
        if char not in counts_dict:
            counts_dict[char] = 0
        counts_dict[char] += 1
    for key, value in counts_dict.items():
        print(key, value)
counts_char(STR_VAL)