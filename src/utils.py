import os
from typing import List
import json

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", 'data', 'operations.json')


def get_data_from_json(path: str) -> List[dict]:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='utf-8') as data_file:
            try:
                transactions = json.load(data_file)
                return transactions
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


a = get_data_from_json(PATH_TO_FILE)
print(a)
