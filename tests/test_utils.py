from unittest.mock import MagicMock, Mock, mock_open, patch

from src.utils import get_amount_in_rub, get_data_from_json


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_get_data_from_json(mock_file: MagicMock) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_data_from_empty_json(mock_file: MagicMock) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_get_data_from_json_not_list(mock_file: MagicMock) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data='{amount": 100}')
def test_get_data_from_json_encode_error(mock_file: MagicMock) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file: MagicMock) -> None:
    transactions = get_data_from_json("data/operations.json")
    assert transactions == []


def test_get_amount_not_rub(transaction_in_usd: dict) -> None:
    mock_conversion = Mock(return_value=123.45)
    get_amount_in_rub = mock_conversion
    assert get_amount_in_rub(transaction_in_usd) == 123.45
    mock_conversion.assert_called()


@patch("src.utils.get_amount_in_rub")
def test_get_amount_not_rub1(mock: MagicMock, transaction_data_1: dict) -> None:
    mock.return_value = 0.0
    assert get_amount_in_rub(transaction_data_1) == 0.0


def test_get_amount_in_rub(transaction_in_rub: dict) -> None:
    assert get_amount_in_rub(transaction_in_rub) == 43318.34


def test_get_amount_in_rub_except() -> None:
    assert get_amount_in_rub({}) == "Транзакция не найдена"
