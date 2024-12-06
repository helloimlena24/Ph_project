
def add_numbers(a, b):
    """Функция, которая складывает два числа."""

    return a


help(add_numbers)


# аннотация типов
def sort_names(names: list[str]) -> list[str]:
    """Функция, которая сортирует список имён."""
    return sorted(names)


# модуль typing
# Union исп. когда указываем несколько вар. типов данных на вход
from typing import Union


def calculation(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    ### функция, которая складывает 2 числа ###
    return a + b


def sum_of_values(value_1, value_2):
    """
    Функция, суммирующая два числа
    """
    summa = value_1 + value_2
    return summa


def sub_of_values(value_1, value_2):
    """
    Функция, вычитающая два числа
    """
    subtract = value_1 - value_2
    return subtract


