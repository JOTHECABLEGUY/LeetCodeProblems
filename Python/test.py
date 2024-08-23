from fib import fib
import pytest

@pytest.mark.parametrize("num, expected", [
    (0, 0),  # happy path: first Fibonacci number
    (1, 1),  # happy path: second Fibonacci number
    (2, 1),  # happy path: third Fibonacci number
    (3, 2),  # happy path: fourth Fibonacci number
    (10, 55),  # happy path: larger Fibonacci number
    (20, 6765),  # happy path: even larger Fibonacci number
    (30, 832040),  # happy path: even large Fibonacci number
], ids=[
    "fib_0", "fib_1", "fib_2", "fib_3", "fib_10", "fib_20", "fib_30"
])
def test_fib_happy_path(num, expected):

    # Act
    result = fib(num)

    # Assert
    assert result == expected

@pytest.mark.parametrize("num", [
    -1,  # edge case: negative number
], ids=[
    "fib_negative"
])
def test_fib_negative(num):

    # Act
    with pytest.raises(ValueError):
        fib(num)

@pytest.mark.parametrize("num", [
    "string",  # error case: string input
    5.5,  # error case: float input
    None,  # error case: None input
], ids=[
    "fib_string", "fib_float", "fib_none"
])
def test_fib_error_cases(num):

    # Act
    with pytest.raises(TypeError):
        fib(num)
