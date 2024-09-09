from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    Декоратор принимает необязательный аргумент filename с расширением ".txt",
    который определяет, куда будут записываться логи (в файл или в консоль)."""

    def logging(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} - ok\n")
                else:
                    print(f"{func.__name__} - ok")
            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error} Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error} Inputs: {args}, {kwargs}")
                raise

            return result

        return wrapper

    return logging
