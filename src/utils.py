import json
from datetime import datetime
from pathlib import Path


def load_date(json_file):
    """ Функция открытя JSON файла """
    BASE_PATH = Path(__file__).parent
    OPERATIONS_PATH_FILE = BASE_PATH.joinpath(json_file)
    with open(OPERATIONS_PATH_FILE, 'r') as file:
        list_of_operations = json.loads(file.read())
        return list_of_operations


def executed_operation(list_of_operation):
    """Функция отбирающей только по EXECUTED"""
    executed_list = []
    for operation in list_of_operation:
        if operation.get('state') == 'EXECUTED':
            executed_list.append(operation)
    return executed_list


def last_five_operation(list_of_operations):
    """ Функция сортирующая по дате последние 5 операций """
    sorted_date = sorted(list_of_operations, key=lambda x: x.get('date', ''), reverse=True)
    last_operation = sorted_date[:5]
    return last_operation


def sorted_date(list_operations):
    """ Функция меняющая формат времени """
    for operation in list_operations:
        operation['date'] = datetime.fromisoformat(operation['date']).strftime('%d.%m.%Y')
    return list_operations


def hiding_card_number(card_number):
    """ Функция маскирующая номер карты и счета """
    card = card_number.split()[-1]
    if len(card) == 16:
        number_card = card[:6] + (len(card[6:12]) * '*') + card[-4:]
        masked_number_card = f'{card_number[:-len(card)]}{" ".join(number_card[i:i + 4] for i in range(0, 16, 4))}'
    else:
        masked_number_card = f'{card_number[:-len(card)]}{"**" + card[-4:]}'
    return masked_number_card
