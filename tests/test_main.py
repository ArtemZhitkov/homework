from typing import Any
from unittest.mock import MagicMock, patch

from main import (PATH_TO_FILE, choice_status, get_data_from_json, greeting, main, only_rub, output_result,
                  sorting_by_date)


@patch("builtins.input", side_effect="1")
def test_greeting(mock: MagicMock) -> None:
    assert greeting() == get_data_from_json(PATH_TO_FILE)


@patch("builtins.input", side_effect=["CANCELED"])
def test_choice_status_1(mock: MagicMock, data_transaction: list) -> None:
    assert choice_status(data_transaction) == [
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        }
    ]


@patch("builtins.input", side_effect=["PENDING"])
def test_choice_status_2(mock: MagicMock, data_transaction: list) -> None:
    assert choice_status(data_transaction) == []


@patch("builtins.input", side_effect=["EXECUTED"])
def test_choice_status_3(mock: MagicMock, data_transaction: list) -> None:
    assert choice_status(data_transaction) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@patch("builtins.input", side_effect=["нет"])
def test_empty_transactions(mock: MagicMock) -> None:
    assert sorting_by_date([]) == []


@patch("builtins.input", side_effect=["да", "по возрастанию"])
def test_sorting_by_date(mock: MagicMock, data_transaction: list) -> None:
    assert sorting_by_date(data_transaction) == [
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
    ]


@patch("builtins.input", side_effect=["да"])
def test_only_rub(mock: MagicMock, data_transaction: list) -> None:
    assert only_rub(data_transaction) == [
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
    ]


@patch("builtins.input", side_effect=["нет"])
def test_only_rub_2(mock: MagicMock, data_transaction: list) -> None:
    assert only_rub(data_transaction) == [
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
    ]


@patch("builtins.input", side_effect=["да", "перевод"])
def test_sorting_by_word(mock: MagicMock, data_transaction: list) -> None:
    assert sorting_by_date(data_transaction) == [
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
    ]


@patch("builtins.input", side_effect=["нет"])
def test_sorting_by_word_2(mock: MagicMock, data_transaction: list) -> None:
    assert sorting_by_date(data_transaction) == [
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2019-03-23T01:09:46.296404",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
            "state": "EXECUTED",
            "to": "Счет 74489636417521191160",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_output_result(capsys: Any, data_transaction: list) -> None:
    output_result(data_transaction)
    out, err = capsys.readouterr()
    assert out == (
        "Программа: Распечатываю итоговый список транзакций...\n"
        "Всего банковских операций в выборке: 5\n"
        "30.06.2018 Перевод организации\n"
        "Счет **6702 -> Счет **6952\n"
        "Сумма: 9824.07\n"
        "04.04.2019 Перевод со счета на счет\n"
        "Счет **4188 -> Счет **8542\n"
        "Сумма: 79114.93\n"
        "23.03.2019 Перевод со счета на счет\n"
        "Счет **1160 -> Счет **4719\n"
        "Сумма: 43318.34\n"
        "19.08.2018 Перевод с карты на карту\n"
        "Visa Platinum 8990 92** **** 5229 -> Visa Classic 6831 98** **** 7658\n"
        "Сумма: 56883.54\n"
        "12.09.2018 Перевод организации\n"
        "Счет **1657 -> Visa Platinum 1246 37** **** 3588\n"
        "Сумма: 67314.70\n"
    )


def test_output_result_empty(capsys: Any) -> None:
    output_result([])
    out, err = capsys.readouterr()
    assert out == "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"


@patch("builtins.input", side_effect=["1", "CANCELED", "да", "да", "по возрастанию", "да", "да", "перевод"])
def test_main(mock: MagicMock, capsys: Any) -> None:
    main()
    out, err = capsys.readouterr()
    assert out == (
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
        "Для обработки выбран JSON-файл.\n"
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        "Операции отфильтрованы по статусу CANCELED\n"
        "Выводить только рублевые транзакции? Да/Нет\n"
        "Отфильтровать список транзакций по определенному слову описании? Да/Нет\n"
        "Программа: Распечатываю итоговый список транзакций...\n"
        "Всего банковских операций в выборке: 1\n"
        "18.04.2019 Открытие вклада\n"
        "Счет **4865\n"
        "Сумма: 73778.48\n"
    )


@patch("builtins.input", side_effect=["1", "PENDING", "да", "да", "по возрастанию", "да", "да", "вклад"])
def test_main_2(mock: MagicMock, capsys: Any) -> None:
    main()
    out, err = capsys.readouterr()
    assert out == (
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
        "Для обработки выбран JSON-файл.\n"
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        "Операции отфильтрованы по статусу PENDING\n"
        "Выводить только рублевые транзакции? Да/Нет\n"
        "Отфильтровать список транзакций по определенному слову описании? Да/Нет\n"
        "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации\n"
    )
