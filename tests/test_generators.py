from typing import List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(data_transaction: List[dict]) -> None:
    assert next(filter_by_currency(data_transaction, "USD")) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency_rub(data_transaction: List[dict]) -> None:
    assert next(filter_by_currency(data_transaction, "RUB")) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_by_currency_any(data_transaction: List[dict]) -> None:
    with pytest.raises(StopIteration):
        next(filter_by_currency(data_transaction, "TEN"))

    with pytest.raises(StopIteration):
        next(filter_by_currency(data_transaction, "CNY"))

    with pytest.raises(StopIteration):
        next(filter_by_currency(data_transaction, "BYN"))


def test_filter_by_currency_empty() -> None:
    with pytest.raises(StopIteration):
        next(filter_by_currency([], "EUR"))


def test_transaction_descriptions(data_transaction: List[dict]) -> None:
    generator = transaction_descriptions(data_transaction)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"

    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions_empty() -> None:
    with pytest.raises(StopIteration):
        next(transaction_descriptions([]))


def test_card_number_generator() -> None:
    generator = card_number_generator(1, 5)

    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"

    with pytest.raises(StopIteration):
        next(generator)
