def get_mask_card_number(card_number: str) -> str | None:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера."""
    if len(card_number) == 16:
        return f"{card_number[:3]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return None


def get_mask_account(card_number: str) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
     где X — это цифра номера."""
    if len(card_number) == 16:
        return f"**{card_number[12:]}"
    else:
        return None
