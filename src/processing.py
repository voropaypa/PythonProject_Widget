from typing import Union


def filter_by_state(list_of_dictionaries: Union[list], key: Union[str] = 'EXECUTED') -> Union[list]:
    """Функция сортирует по статусу исполнения.
    Функция получает на вход список словарей и ключ, и возвращает только те словари,
    у которых статус(state) соответствует заданному функцией условию(key, по умолчанию - 'EXECUTED')"""
    new_dict_list = list()
    for dictionary in list_of_dictionaries:
        if dictionary["state"] == key:
            new_dict_list.append(dictionary)
    if new_dict_list == []:
        raise KeyError("Операций с таким статусом не обнаружено.")
    return new_dict_list


def sort_by_date(list_of_dicts: Union[list], reverse: bool = True) -> Union[list]:
    """Функция сортирует по дате исполнения.
    Функция получает на вход список словарей и порядок сортировки (по умолчанию - по убыванию),
    и возвращает словари в заданном порядке, сортируя их по дате(ключ 'date')"""
    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse)
