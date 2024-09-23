import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

PATH_TO_FILE = os.path.join("..", ".env")
load_dotenv(PATH_TO_FILE)

API_KEY = os.getenv("API_KEY")


def currency_conversion_in_rub(transaction: Dict) -> float | Any:
    """Функция, которая обращается к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""

    headers = {"apikey": API_KEY}
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"

    response = requests.get(url, headers=headers)

    result = response.json()
    return float(result["result"])
