from typing import Union

from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(card_info: Union[str]) -> Union[str]:
    card_alpha = ""
    card_digit = ""
    for symbol in card_info:
        if symbol.isalpha():
            card_alpha += symbol
        if symbol == " ":
            card_alpha += symbol
        elif symbol.isdigit():
            card_digit += symbol
    if len(card_digit) == 16:
        card_mask = get_mask_card_number(card_digit)
    elif len(card_digit) == 20:
        card_mask = get_mask_account(card_digit)
    return card_alpha + card_mask


def get_date(date_data: Union[str]) -> Union[str]:
    return f"{date_data[8:10]}.{date_data[5:7]}.{date_data[:4]}"


# print(get_date("2024-03-11T02:26:18.671407"))
# print(mask_account_card("Счет 73654108430135874305"))
