from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX,
    где X — это цифра номера."""
    if card_number == "":
        raise ValueError("Ошибка. Пустой ввод.")
    elif isinstance(card_number, str):
        raise TypeError("Ошибка. Введён неправильный тип данных.")

    card_number_str = str(card_number)

    if len(card_number_str) != 16:
        raise ValueError("Ошибка. Номер карты введён неверно.")

    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"


def get_mask_account(account_number: Union[int]) -> Union[str]:
    """Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера."""
    if account_number == "":
        raise ValueError("Ошибка. Пустой ввод.")
    elif isinstance(account_number, str):
        raise TypeError("Ошибка. Введён неправильный тип данных.")

    account_number_str = str(account_number)

    if len(account_number_str) != 20:
        raise ValueError("Ошибка. Номер счёта введён неверно.")

    return f"**{account_number_str[-4:]}"
