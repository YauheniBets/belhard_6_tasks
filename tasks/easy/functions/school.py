"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}
def incr_students(data: dict, name_of_class: str):
    data[name_of_class] += 1
    return data
print(incr_students(school_data, '1a'))

def decr_students(data: dict, name_of_class: str):
    if data[name_of_class] != 0:
        data[name_of_class] -= 1
        return data
    raise RuntimeError('В классе нет учеников')
print(decr_students(school_data, '1a'))

def add_class(data: dict, name_of_class: str):
    if name_of_class not in data:
        data[name_of_class] = 0
        return data
    raise ('Такой класс уже в списке')
print(add_class(school_data, '3a'))

def remove_class(data: dict, name_of_class: str):
    if name_of_class in data:
        data.pop(name_of_class)
        return data
    raise KeyError('Такого класса нет в списке')
print(remove_class(school_data, '3a'))

def calc_students(data: dict):
    data = sum(data.values())
    return data
print(calc_students(school_data))




