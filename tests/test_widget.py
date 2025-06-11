import pytest
from src.widget import mask_account_card


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