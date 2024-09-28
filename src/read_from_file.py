import logging
import os

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/read_from_file.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("read_from_file")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

PATH_TO_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
PATH_TO_EXCEL = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def read_from_csv(path: str, sep: str = ";") -> list:
    """Функция, которая принимает на вход путь к файлу с транзакциями в формате .csv и возвращает
    список словарей с транзакциями"""
    try:
        logger.info(f"Чтение файла {path}")
        df = pd.read_csv(path, sep=sep)
        logger.info("Возврат списка словарей с транзакциями")
        return df.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        logger.warning(f"Ошибка: Файл {path} пустой.")
        return []
    except FileNotFoundError:
        logger.warning(f"Файл {path} не найден.")
        return []


def read_from_excel(path: str, sheet_name: int = 0) -> list:
    """Функция, которая принимает на вход путь к excel-файлу с транзакциями и возвращает
    список словарей с транзакциями"""
    try:
        logger.info(f"Чтение файла {path}")
        df = pd.read_excel(path, sheet_name=sheet_name)
        logger.info("Возврат списка словарей с транзакциями")
        return df.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        logger.warning(f"Ошибка: Лист {sheet_name} в файле {path} пустой.")
        return []

    except FileNotFoundError:
        logger.warning(f"Файл {path} не найден.")
        return []
