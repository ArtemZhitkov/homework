from typing import Any

import pytest

from src.decorators import log


@log()
def function_success(x: int, y: int) -> int:
    return x + y


@log()
def function_error() -> None:
    raise ValueError("Test error")


def test_log_success(capsys: Any) -> None:
    function_success(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "function_success - ok\n"


def test_log_error(capsys: Any) -> None:
    with pytest.raises(Exception, match="Test error"):
        function_error()

    captured = capsys.readouterr()
    assert captured.out == "function_error error: Test error Inputs: (), {}\n"


def test_log_to_file() -> None:
    @log(filename="test_log.txt")
    def function_file_success(x: int, y: int) -> int:
        return x + y

    @log(filename="test_log.txt")
    def function_file_error(x: int, y: int) -> None:
        raise ValueError("Test error")

    function_file_success(1, 2)

    with open("test_log.txt", 'r') as file:
        log_content = file.read()

        assert "function_file_success - ok\n" in log_content
        with pytest.raises(Exception):
            function_file_error(1, 2)

        with open("test_log.txt", 'r') as f:
            log_content = f.read()

            assert "function_file_error error: Test error Inputs: (1, 2), {}\n" in log_content
