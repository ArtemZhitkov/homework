import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('card_number, mask_card_number', [('1596837868705199', '1596 83** **** 5199'),
                                                           ('715830073472675', None),
                                                           ('', None),
                                                           (7158300734726758, '7158 30** **** 6758'),
                                                           ('71583007347267581', None)])
def test_get_mask_card_number(card_number: str, mask_card_number: str) -> None:
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize('account_number, masc_account', [('64686473678894779589', '**9589'),
                                                          ('', None),
                                                          (64686473678894779589, '**9589'),
                                                          ('646864736788947795890', None),
                                                          ('646864736788947795', None)])
def test_get_mask_account(account_number: str, masc_account: str) -> None:
    assert get_mask_account(account_number) == masc_account
