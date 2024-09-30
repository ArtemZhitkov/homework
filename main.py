from time import sleep

from src.processing import filter_by_state, search_by_pattern, sort_by_date
from src.read_from_file import PATH_TO_CSV, PATH_TO_EXCEL, read_from_csv, read_from_excel
from src.utils import PATH_TO_FILE, get_data_from_json
from src.widget import get_date, mask_account_card


def greeting() -> list:
    """Функция приветствует и предлагает выбрать из какого файла считать данные
    и возвращает список словарей с транзакциями"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    user_input = input("Введите номер пункта меню: ")
    while True:
        if user_input == "1":
            print("Для обработки выбран JSON-файл.")
            return get_data_from_json(PATH_TO_FILE)
        elif user_input == "2":
            print("Для обработки выбран CSV-файл.")
            return read_from_csv(PATH_TO_CSV)
        elif user_input == "3":
            print("Для обработки выбран EXCEL-файл.")
            return read_from_excel(PATH_TO_EXCEL)
        else:
            print("Пожалуйста, введите число от 1 до 3.")
            user_input = input()


def choice_status(transactions: list) -> list:
    """Функция предлагает по какому статусу отфильтровать транзакции."""

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    user_status = input().upper()

    while True:
        if user_status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {user_status} недоступен.")
            print("Введите статус, по которому необходимо выполнить фильтрацию.")
            print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
            user_status = input().upper()
        else:
            break
    print(f"Операции отфильтрованы по статусу {user_status}")
    return filter_by_state(transactions, user_status)


def sorting_by_date(transactions: list) -> list:
    """Функция предлагает отсортировать транзакции по дате."""

    sorted_by_date = input("Отсортировать операции по дате? Да/Нет").lower()
    if sorted_by_date in ["да", "yes", "lf"]:
        rev = input("Отсортировать по возрастанию или по убыванию?").lower()
        if rev == "по возрастанию":
            return sort_by_date(transactions, is_reverse=False)
        else:
            return sort_by_date(transactions)
    else:
        return transactions


def only_rub(transactions: list) -> list:
    """Функция предлагает выводить только рублевые транзакции или нет"""
    print("Выводить только рублевые транзакции? Да/Нет")
    choice_currency = input().lower()
    if choice_currency in ["да", "yes", "lf"]:
        result = []
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                result.append(transaction)
        return result
    else:
        return transactions


def sorting_by_word(transactions: list) -> list:
    """Функция предлагает отфильтровать транзакции по ключевому слову"""
    print("Отфильтровать список транзакций по определенному слову описании? Да/Нет")
    user_input = input().lower()
    if user_input in ["да", "yes", "lf"]:
        user_word = input("Введите слово для сортировки").lower()
        return search_by_pattern(transactions, user_word)
    else:
        return transactions


def output_result(transactions: list) -> None:
    """Вывод информации по транзакциям с учетом фильтров"""

    if transactions:
        print("Программа: Распечатываю итоговый список транзакций...")
        sleep(1)
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        sleep(1)
        for transaction in transactions:
            date = get_date(transaction.get("date"))
            description = transaction.get("description")
            mask_to = mask_account_card(transaction.get("to"))
            amount = transaction.get("operationAmount")["amount"]

            if description == "Открытие вклада":
                print(f"{date} {description}")
                print(mask_to)
                print(f"Сумма: {amount}")
            else:
                mask_from = mask_account_card(transaction.get("from", "Нет данных"))
                print(f"{date} {description}")
                print(f"{mask_to} -> {mask_from}")
                print(f"Сумма: {amount}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main() -> None:
    start = greeting()
    status = choice_status(start)
    sorting = sorting_by_date(status)
    currency = only_rub(sorting)
    filtered_transactions = sorting_by_word(currency)
    output_result(filtered_transactions)


if __name__ == "__main__":
    main()
