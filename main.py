from src import utils

def main(json_file):
    list_of_operations = utils.load_date(json_file)
    sort_by_executed = utils.executed_operation(list_of_operations)
    five_operations = utils.last_five_operation(sort_by_executed)
    sorted_by_date = utils.sorted_date(five_operations)
    for operation in sorted_by_date:
        if operation.get('from') is not None:
            hiding_card_number_from = utils.hiding_card_number(operation['from'])
            hiding_card_number_to = utils.hiding_card_number(operation['to'])

            print(f'{operation["date"]} {operation["description"]}\n'
                f'{hiding_card_number_from} -> {hiding_card_number_to}\n'
                f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
        else:
            hiding_card_number_to = utils.hiding_card_number(operation['to'])
            print(f'{operation["date"]} {operation["description"]}\n'
                  f'{hiding_card_number_to}\n'
                  f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')

if __name__ == '__main__':
    main('./data/operations.json')

