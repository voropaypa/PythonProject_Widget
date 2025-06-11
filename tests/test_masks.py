import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.fixture
def card_numbers():
    """Примеры номеров карт"""
    return [7000792289606361,
            715830073472678,
            68319824767378,
            899092211366522569,
            5999414228]


@pytest.mark.parametrize("card_number, expected", [
    (7000792289606361, "7000 79** **** 6361"),
    (7158300734726758, "7158 30** **** 6758"),
    (6831982476737658, "6831 98** **** 7658"),
    (8990922113665229, "8990 92** **** 5229"),
    (5999414228426353, "5999 41** **** 6353")
])
def test_get_mask_card_number(card_number, expected):
    """Проверяет работу функции при введении номеров правильного формата"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_wrong_length():
    """Проверяет, что срабатывает вызов ошибки при введении номера карты неправильной длины"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_numbers)


def test_get_mask_card_number_empty_entrance():
    """Проверяет, что срабатывает вызов ошибки при пустом вводе"""
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_card_number_wrong_type():
    """Проверяет, что срабатывает ошибка TypeError, если введен str"""
    with pytest.raises(TypeError):
        get_mask_card_number("Str")


# def test_get_mask_account():
#     assert get_mask_account(73654108430135874305) == "**4305"