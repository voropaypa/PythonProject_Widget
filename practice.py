from typing import Union
from typing import List


def match_numbers(first_list: Union[list], second_list: Union[list]) -> Union[list]:
    """Функция, которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа,
    которые встречаются в обоих списках."""
    matched_numbers = []
    for number in first_list:
        if number in second_list:
            matched_numbers.append(number)
    return matched_numbers


print(match_numbers([1, 2, 3, 4], [3, 4, 5, 6]))


def get_palindromes(list_a: List[int]) -> List[int]:
    """Функция, которая получает на вход список чисел и возвращает новый список,
    содержащий только числа, которые являются палиндромами"""
    palindrome_list = []
    for number in list_a:
        if str(number) == str(number)[::-1]:
            palindrome_list.append(number)
    return palindrome_list


print(get_palindromes([121, 123, 131, 34543]))


def get_unique_numbers(first_list: List[int], second_list: List[int]) -> List[int]:
    """Функция, которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа,
    которые есть только в одном из списков."""
    unique_numbers = []
    for number in first_list:
        if number not in second_list:
            unique_numbers.append(number)
    for number in second_list:
        if number not in first_list:
            unique_numbers.append(number)
    return unique_numbers


print(get_unique_numbers([1, 2, 3, 4], [3, 4, 5, 6]))


def circle_area(r: float) -> float:
    """Считает площадь окружности"""
    pi = 3.14
    circled_area = pi * r**2
    return circled_area


def format_description(r: float, area: float) -> str:
    """Форматирует данные по окружности"""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_circle_info(r: float) -> None:
    """Получение информации об окружности"""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_circle_info(radius)
