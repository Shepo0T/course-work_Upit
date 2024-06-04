import json
from datetime import datetime
import os

def load_date(json_file):
    """ Функция открытя JSON файла """
    file_operations = os.path.abspath(json_file)
    with open(file_operations, 'r') as file:
        list_of_operations = json.loads(file.read())
        return list_of_operations


def last_five_operation(list_of_operations):
    """ Функция сортирующая по дате последние 5 операций """
    sorted_operations = sorted(list_of_operations, key=lambda x: x.get('date', ''))
    last_operation = sorted_operations[-5:]
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

