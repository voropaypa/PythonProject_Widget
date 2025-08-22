from typing import Generator, Union


def filter_by_currency(transactions: Union[list], currency: Union[str]) -> Generator:
    """Функция-генератор, которая принимает на вход список словарей,
    представляющих транзакции. Функция возвращает итератор,
    который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""
    counter = 0
    filter_result = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    if transactions == []:
        raise ValueError("Ошибка. Транзакции не обнаружены.")
    elif len(filter_result) == 0:
        raise ValueError("Ошибка. Транзакций с заданной валютой не найдено.")
    else:
        for transaction in filter_result:
            yield transaction


def transaction_descriptions(transactions: Union[list]) -> Generator:
    """Функция-генератор, которая принимает на вход список словарей,
    представляющих транзакции. Функция возвращает итератор, который поочерёдно
    возвращает описание каждой операции."""
    counter = 0
    descriptions_list = [x["description"] for x in transactions]
    if transactions == []:
        raise ValueError("Ошибка. Транзакции не обнаружены.")
    else:
        for description in descriptions_list:
            yield description


def card_number_generator(start: Union[int], stop: Union[int]) -> Generator:
    """Функция-генератор, которая выдает поочерёдно банковские номера в формате
    "XXXX XXXX XXXX XXXX" в заданном диапазоне от 0000 0000 0000 0001
    до 9999 9999 9999 9999. Генератор принимает начальное и конечное значения
    для генерации диапазона номеров."""
    counter = 0
    if not (0 <= start <= 9999999999999999) or not (0 < stop <= 9999999999999999):
        raise ValueError("Ошибка. Неправильный формат номера")
    else:
        for num in range(start, stop + 1):
            num_line = f"{num:016d}"
            line_with_spaces = " ".join(num_line[i:i+4] for i in range(0, len(num_line), 4))
            yield line_with_spaces
