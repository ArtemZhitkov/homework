import os

import pandas as pd

PATH_TO_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
PATH_TO_EXCEL = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


def read_from_csv(path: str, sep: str = ";") -> list | None:
    """Функция, которая принимает на вход путь к файлу с транзакциями в формате .csv и возвращает
    список словарей с транзакциями"""
    try:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Файл {path} не найден.")

        df = pd.read_csv(path, sep=sep)
        return df.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        print(f"Ошибка: Файл {path} пустой.")
        return None
    except pd.errors.ParserError as e:
        print(f"Ошибка парсинга: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


def read_from_excel(path: str, sheet_name: int = 0) -> list | None:
    """Функция, которая принимает на вход путь к excel-файлу с транзакциями и возвращает
    список словарей с транзакциями"""
    try:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Файл {path} не найден.")

        df = pd.read_excel(path, sheet_name=sheet_name)
        return df.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        print(f"Ошибка: Лист {sheet_name} в файле {path} пустой.")
        return None

    except Exception as e:
        print(f"Неожиданная ошибка при чтении Excel файла: {e}")
        return None


print(read_from_csv(PATH_TO_CSV))
