from unittest.mock import mock_open, patch

from src.utils import get_amount_in_rub, get_data_from_json


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_get_data_from_json(mock_file) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_data_from_empty_json(mock_file) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_get_data_from_json_not_list(mock_file) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data='{amount": 100}')
def test_get_data_from_json_encode_error(mock_file) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


@patch("currency_conversion_in_rub")
def test_get_amount_in_rub_from_usd(mock) -> None:
    result = get_amount_in_rub(
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        }
    )
    assert result == 1.0


def test_get_amount_in_rub(transaction_in_rub) -> None:
    assert get_amount_in_rub(transaction_in_rub) == 43318.34


def test_get_amount_in_rub_except() -> None:
    assert get_amount_in_rub({}) == "Транзакция не найдена"
