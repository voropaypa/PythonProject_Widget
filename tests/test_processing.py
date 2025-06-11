import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def example_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_state_with_no_lists():
    """Проверка работы функции - фильтрации - при корректном вводе данных, но
    при отсутствии словарей с заданным статусом state"""
    with pytest.raises(KeyError):
        assert filter_by_state(
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}],
            "CANCELED")


def test_filter_by_state_with_no_given_state(example_list):
    """Проверка работы функции - фильтрации - при корректном вводе данных
    без заданного статуса state"""
    assert filter_by_state(example_list) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize("example_status, expected_list", [
    ('EXECUTED',
     [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ('CANCELED',
     [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
])
def test_filter_by_state(example_list, example_status, expected_list):
    """Проверка работы функции - фильтрации - при корректном вводе данных
    с заданным статусом state"""
    assert filter_by_state(example_list, example_status) == expected_list