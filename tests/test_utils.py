from pathlib import Path
from src import utils
import pytest


def test_load_date():
    """ Tест на проверку несуществующего файла"""
    BASE_PATH = Path(__file__).parent
    OPERATIONS_PATH_FILE = BASE_PATH.joinpath("operations.json")
    with pytest.raises(FileNotFoundError):
        utils.load_date(OPERATIONS_PATH_FILE)


def test_executed_operation():
    """Тест функции отбирающей только по EXECUTED"""
    assert utils.executed_operation(
        [{"state": "EXECUTED", "amount": "31957.58"}, {"state": "CANCELED", "amount": "67314.70"},
         {"state": "EXECUTED", "amount": "90582.51"}]) == [{"state": "EXECUTED", "amount": "31957.58"},
                                                           {"state": "EXECUTED", "amount": "90582.51"}]


def test_last_five_operations():
    """ Проверка на сортировку 5 последних выполненых операций """

    assert utils.last_five_operation([{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]) == [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]


def test_sorted_date():
    """ Проверка функции перевода времени """
    date = [{"date": "2018-01-21T01:10:28.317704"}]
    assert utils.sorted_date(date) == [{'date': '21.01.2018'}]


def test_hiding_card_number():
    """ Проверка функции скрывания номера карт и счетов """
    assert utils.hiding_card_number('Счет 33407225454123927865') == 'Счет **7865'
    assert utils.hiding_card_number('Visa Classic 4195191172583802') == 'Visa Classic 4195 19** **** 3802'
