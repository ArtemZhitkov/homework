import pytest

from src.processing import filter_by_state, sort_by_date, search_by_pattern, counter_description


@pytest.mark.parametrize(
    "data, expected",
    [
        (
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        ),
        ([], []),
    ],
)
def test_filter_by_state(data: list, expected: list) -> None:
    assert filter_by_state(data) == expected


def test_filter_by_state_canceled(data_list: list) -> None:
    assert filter_by_state(data_list, key="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "data, expected",
    [
        (
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        ),
        (
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2019-07-030T02:08:58.425572"},
                    {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
                ],
                [
                    {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2019-07-030T02:08:58.425572"},
                ],
        ),
        ([], []),
    ],
)
def test_sort_by_date(data: list, expected: list) -> None:
    assert sort_by_date(data) == expected


def test_sort_by_date_revers(data_list: list) -> None:
    assert sort_by_date(data_list, is_reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_search_by_pattern(data_transaction: list) -> None:
    assert search_by_pattern(data_transaction, "Visa") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
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
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert search_by_pattern(data_transaction, "вклад") == []
    assert search_by_pattern([], "счет") == []


def test_counter_description(data_transaction: list, description_list: list) -> None:
    assert counter_description(data_transaction, description_list) == {'Перевод организации': 2,
                                                                       'Перевод со счета на счет': 2,
                                                                       'Перевод с карты на карту': 1}
    assert counter_description([], []) == {}
