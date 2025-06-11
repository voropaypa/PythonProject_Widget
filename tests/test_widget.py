import pytest
from src.widget import mask_account_card
from src.widget import get_date


@pytest.fixture
def wrong_numbers_for_widget():
    """Примеры неправильного ввода данных счета или карты"""
    return ["Visa Platinum 70007922896361",
            "6831982476737658",
            "Visa Platinum 700070631",
            "73654108430135874305",
            "Счет 35383047895560",]


@pytest.mark.parametrize("data, mask", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(data, mask):
    """Проверяет работу функции при введении корректных данных о карте или счете"""
    assert mask_account_card(data) == mask


def test_mask_account_card_wrong_entrance():
    """Проверяет, что срабатывает вызов ошибки при неправильном вводе данных, а также
    правильность сочетания вида входных данных - названия карты и его номера
    или названия счета и его номера."""
    with pytest.raises(ValueError):
        mask_account_card(wrong_numbers_for_widget)


def test_mask_account_card_empty_entrance():
    """Проверяет, что срабатывает вызов ошибки при пустом вводе"""
    with pytest.raises(ValueError):
        mask_account_card("")


@pytest.mark.parametrize("date_example, date_result", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2025-02-20T02:26:18.671407", "20.02.2025"),
    ("2016-11-01T02:26:18.671407", "01.11.2016"),
])
def test_get_date(date_example, date_result):
    """Проверяет работу функции с корректными входными данными"""
    assert get_date(date_example) == date_result


@pytest.fixture
def wrong_examples_for_date():
    """Примеры неправильного ввода даты"""
    return ["2024-03-11T02:26:18",
            "2025-02-20T02:26:18.671407",
            "2:26:18.671407",
            "73654108430135874305",
            "Счет 35383047895560",]

def test_get_date_wrong_date():
    """Проверяет, что срабатывает вызов ошибки при некорректном вводе даты"""
    with pytest.raises(ValueError):
        assert get_date(wrong_examples_for_date)


def test_get_date_empty():
    """Проверяет, что срабатывает вызов ошибки при пустом вводе даты"""
    with pytest.raises(ValueError):
        assert get_date("")
