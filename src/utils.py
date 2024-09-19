import json
import os
from typing import List, Any

from src.external_api import currency_conversion_in_rub

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_data_from_json(path: str) -> List[dict] | Any:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    try:
        with open(path, encoding="utf-8") as data_file:
            try:
                transactions = json.load(data_file)
                return transactions
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def get_amount_in_rub(transaction: dict, currency: str = "RUB") -> float | Any:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и
     конвертации суммы операции в рубли."""

    try:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            return transaction.get("operationAmount").get("amount")
        elif transaction["operationAmount"]["currency"]["code"] == "USD":
            return currency_conversion_in_rub(transaction)
        elif transaction["operationAmount"]["currency"]["code"] == "EUR":
            return currency_conversion_in_rub(transaction)
    except KeyError:
        return "Транзакция не найдена"
