import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


def test_filter_by_currency(transactions):
    """Проверка работы функции-генератора при корректном вводе данных
    и наличии транзакций в заданной валюте"""
    generator_usd = filter_by_currency(transactions, "USD")
    assert next(generator_usd) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    generator_rub = filter_by_currency(transactions, "RUB")
    assert next(generator_rub) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }


def test_filter_by_currency_without_transactions(transactions):
    """Проверка работы функции-генератора при отсутствии транзакций
    или операций в заданной валюте"""
    generator_eur = filter_by_currency(transactions, "EUR")
    with pytest.raises(ValueError):
        assert next(generator_eur)


def test_filter_by_currency_end_func(transactions):
    """Проверка работы функции-генератора при его вызове, когда
    все операции уже были выведены"""
    generator_rub = filter_by_currency(transactions, "RUB")
    assert next(generator_rub)
    assert next(generator_rub)
    with pytest.raises(ValueError):
        assert next(generator_rub)


def test_filter_by_currency_empty():
    """Проверка работы функции-генератора при обработке пустого списка"""
    generator = filter_by_currency([], "EUR")
    with pytest.raises(ValueError):
        assert next(generator)


def test_transaction_descriptions(transactions):
    """Проверка работы функции-генератора при корректном вводе данных
    и выводе соответствующих описаний"""
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions_empty(transactions):
    """Проверка работы функции-генератора при вводе пустого списка
    транзакций"""
    generator = transaction_descriptions([])
    with pytest.raises(ValueError):
        assert next(generator)


def test_transaction_descriptions_end_func(transactions):
    """Проверка работы функции-генератора при его вызове, когда
    все операции уже были выведены"""
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    with pytest.raises(ValueError):
        assert next(generator)


def test_card_number_generator():
    """Проверка вывода чисел с помощью функции-генератора
    при корректном вводе данных"""
    generator_first_nums = card_number_generator(0, 2)
    assert next(generator_first_nums) == "0000 0000 0000 0000"
    assert next(generator_first_nums) == "0000 0000 0000 0001"
    generator_other_nums = card_number_generator(99998, 99999)
    assert next(generator_other_nums) == "0000 0000 0009 9998"
    assert next(generator_other_nums) == "0000 0000 0009 9999"


def test_card_number_generator_wrong_nums():
    """Проверка работы функции-генератора при некорректном вводе данных - значений, не входящих в допустимые"""
    generator = card_number_generator(10000000000000000, 10000000000000001)
    with pytest.raises(ValueError):
        assert next(generator)


@pytest.mark.parametrize("start, end", [
    (0, 1),
    (9998, 9999)
])
def test_card_number_generator_end(start, end):
    """Проверка завершения работы итерации"""
    generator = card_number_generator(start, end)
    assert next(generator)
    assert next(generator)
    with pytest.raises(ValueError):
        assert next(generator)
