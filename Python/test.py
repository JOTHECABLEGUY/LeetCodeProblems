# run tests with `pytest path/to/test.py`

from fib import fib
from stack import Stack
import pytest

# ------------------------- { FIB TESTS } -----------------------------
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


# ------------------------- { Stack TESTS } -----------------------------

@pytest.fixture
def stack():
    return Stack()

@pytest.mark.parametrize("elem", ["a", "b", "c"], ids=["push_a", "push_b", "push_c"])
def test_push(stack, elem):
    # Act
    stack.push(elem)
    
    # Assert
    assert stack.data[-1] == elem

@pytest.mark.parametrize("initial_data, expected", [
    (["a", "b", "c"], "c"),
    (["x", "y"], "y"),
    (["single"], "single")
], ids=["pop_c", "pop_y", "pop_single"])
def test_pop(stack, initial_data, expected):
    # Arrange
    stack.data = initial_data.copy()
    
    # Act
    result = stack.pop()
    
    # Assert
    assert result == expected
    assert stack.data == initial_data[:-1]

@pytest.mark.parametrize("initial_data, expected", [
    (["a", "b", "c"], "a b c"),
    (["x", "y"], "x y"),
    ([], "")
], ids=["to_string_abc", "to_string_xy", "to_string_empty"])
def test_to_string(stack, initial_data, expected):
    # Arrange
    stack.data = initial_data.copy()
    
    # Act
    result = stack.to_string()
    
    # Assert
    assert result == expected

@pytest.mark.parametrize("initial_data, expected", [
    (["a", "b", "c"], ["a", "b", "c"]),
    (["x", "y"], ["x", "y"]),
    ([], [])
], ids=["to_list_abc", "to_list_xy", "to_list_empty"])
def test_to_list(stack, initial_data, expected):
    # Arrange
    stack.data = initial_data.copy()
    
    # Act
    result = stack.to_list()
    
    # Assert
    assert result == expected

@pytest.mark.parametrize("initial_data, expected", [
    (["a", "b", "c"], False),
    ([], True)
], ids=["is_empty_false", "is_empty_true"])
def test_is_empty(stack, initial_data, expected):
    # Arrange
    stack.data = initial_data.copy()
    
    # Act
    result = stack.is_empty()
    
    # Assert
    assert result == expected

def test_pop_empty_stack(stack):
    # Act & Assert
    with pytest.raises(IndexError):
        stack.pop()
