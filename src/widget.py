from src.masks import get_mask_account, get_mask_card_number


def get_mask_account_card(card_number: str) -> str:
    """Функция принимает один аргумент — строку, содержащую тип и номер карты или счета,
    возвращает строку с замаскированным номером.
    Для карт и счетов используйте разные типы маскировки"""
    # переменная с номером счета или карты
    account_number: str = ""
    # переменная с названием карты или счета
    card_name: str = ""
    # цикл по входной строке, который разделяет название карты и номер
    for i in card_number:
        if i.isdigit():
            account_number += i
        else:
            card_name += i

    if len(account_number) == 20:
        return f"{card_name}{get_mask_account(account_number)}"
    else:
        return f"{card_name}{get_mask_card_number(account_number)}"


def get_date(date_string: str) -> str:
    """Функция возвращает дату в формате "ДД.ММ.ГГГГ"."""
    date = date_string[:10].split("-")
    return ".".join(reversed(date))


print(get_mask_account_card("Maestro 7000792289606361"))
