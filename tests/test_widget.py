import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('card_number, mask_account',
                         [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                          ('Счет 64686473678894779589', 'Счет **9589'),
                          ('', None),
                          ('Счет 18986161661587457', None),
                          ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                          ('MasterCard 715830073472675844', None),
                          ('MasterCard 71583007347267', None)])
def test_mask_account_card(card_number: str, mask_account: str) -> None:
    assert mask_account_card(card_number) == mask_account


@pytest.mark.parametrize('date, format_date', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                               ('2020-05-30-15:59:02', '30.05.2020'),
                                               ('30-05-2020', '30.05.2020'),
                                               ('', 'Не верный формат даты'),
                                               ('2024-03', 'Не верный формат даты')])
def test_get_date(date:str, format_date: str) -> None:
    assert get_date(date) == format_date
