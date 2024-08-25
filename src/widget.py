from masks import get_mask_card_number


def get_mask_account_card(card_number: str) -> str:
    account_number = ''
    card_name = ''
    for i in card_number:
        if i.isdigit():
            account_number += i
        else:
            card_name += i
    if len(account_number) == 20:
        return f'{card_name}**{account_number[-4:]}'
    else:
        return f'{card_name}{get_mask_card_number(account_number)}'


def get_date(date_string: str) -> str:
    date = date_string[:10].split('-')
    return '.'.join(reversed(date))
