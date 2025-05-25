from typing import Union


def get_mask_card_number(card_number: Union[int]) -> Union[str]:
    """Принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX,
    где X — это цифра номера."""
    card_number_str = str(card_number)
    return f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"


def get_mask_account(account_number: Union[int]) -> Union[str]:
    """Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера."""
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"


# print(get_mask_card_number(7000792289606361))
# print(get_mask_account(73654108430135874305))
