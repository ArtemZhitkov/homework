import json
import logging
import os
from typing import Any, List

from src.external_api import currency_conversion_in_rub

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..\\logs\\utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_data_from_json(path: str) -> List[dict] | Any:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    try:
        logger.info("Открытие файла: operations.json")
        with open(path, encoding="utf-8") as data_file:
            try:
                logger.info("Преобразование транзакций из JSON-формата в список словарей")
                transactions = json.load(data_file)
                if isinstance(transactions, list):
                    return transactions
                else:
                    logger.warning("Файл пустой")
                    return []
            except json.JSONDecodeError as ex:
                logger.error(f"Произошла ошибка: {ex}")
                return []
    except FileNotFoundError:
        logger.error("Произошла ошибка: FileNotFoundError")
        return []


def get_amount_in_rub(transaction: dict) -> float | str:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и
     конвертации суммы операции в рубли."""

    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            logger.info("Возврат суммы транзакции")
            return float(transaction["operationAmount"]["amount"])
        else:
            logger.info("Вызов функции конвертации валюты")
            return currency_conversion_in_rub(transaction)
    except KeyError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return "Транзакция не найдена"
