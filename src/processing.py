def filter_by_state(list_dicts: list, key: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей
    и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""

    return [i for i in list_dicts if i["state"] == key]


def sort_by_date(list_dicts: list, revers: bool = True) -> list:
    """Функцию, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date)."""

    return sorted(list_dicts, key=lambda x: x["date"], reverse=revers)
