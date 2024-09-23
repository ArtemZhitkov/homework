from unittest.mock import patch

from src.external_api import currency_conversion_in_rub


@patch('requests.get')
def test_currency_conversion_in_rub(mock_get):
    mock_get.return_value.json.return_value["result"] = 1.0
    assert currency_conversion_in_rub({"operationAmount": {
        "amount": "1.0",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    }
    }) == 1.0
    mock_get.assert_called()
