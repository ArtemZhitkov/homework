import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..\\logs\\masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str | None:
    """Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера."""
    card_number = str(card_number)
    if len(card_number) == 16:
        logger.info("Маскировка номера карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        logger.warning(f"Неверный номер карты: длина номера - {len(card_number)}")
        return None


def get_mask_account(account_number: str) -> str | None:
    """Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX,
     где X — это цифра номера."""
    account_number = str(account_number)
    if len(account_number) == 20:
        logger.info("Маскировка номера счета")
        return f"**{account_number[-4:]}"
    else:
        logger.warning(f"Неверный номер счета: длина номера - {len(account_number)}")
        return None
