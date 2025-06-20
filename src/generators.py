from typing import Union


def filter_by_currency(transactions: Union[list], currency: Union[str]) -> Union[list]:
    filter_result = [x for x in transactions if x["operationAmount"]["currency"]["name"] == currency]
    for transaction in filter_result:
        yield transaction


def transaction_descriptions(transactions: Union[list]) -> Union[str]:
    descriptions_list = [x["description"] for x in transactions]
    for description in descriptions_list:
        yield description


def card_number_generator(num1: Union[int], num2: Union[int]) -> Union[str]:
    for num in range(num1, num2 + 1):
        num_line = f"{num:016d}"
        line_with_spaces = " ".join(num_line[i:i+4] for i in range(0, len(num_line), 4))
        yield line_with_spaces
        num += 1
