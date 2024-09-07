from typing import Iterator, List


def filter_by_currency(transactions_list: List[dict], currency: str) -> Iterator[dict]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
        Функция возвращает итератор, который поочередно выдает транзакции,
        где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Iterator[dict]:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions_list:
        operation = transaction.get("description", "Нет данных")
        yield operation


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор принимает начальное и конечное значения для генерации диапазона номеров."""
    for number in range(start, stop + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        yield f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}'
