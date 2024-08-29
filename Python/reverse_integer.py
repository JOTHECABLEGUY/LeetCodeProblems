"""7. Reverse Integer
Medium
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1"""
import pytest
class Solution:
    def reverse(self, x:int) -> int:
        """Reverses the digits of the given integer.

            This method takes an integer as input and returns its reverse. 
            If the reversed integer exceeds the 32-bit signed integer range, 
            it returns 0.

            Args:
                x (int): The integer to be reversed.

            Returns:
                int: The reversed integer, or 0 if it exceeds the 32-bit signed integer range.

            Raises:
                ValueError: If the input is not an integer.
        """
        if not isinstance(x, int):
            raise ValueError("Must provide integer input value.")
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = x % 10
        while (x:=x//10):
            res = res * 10 + x % 10
            if res > pow(2, 31)-1:
                return 0
        return res*sign

@pytest.mark.parametrize("input_value, expected_output", [
    # Happy path tests
    (123, 321),
    (-123, -321),
    (120, 21),
    (0, 0),

    # Edge cases
    (1534236469, 0),
    (-1534236469, 0),
    (2147483647, 0),
    (-2147483648, 0),
], ids = ["positive number", "negative number", "number with trailing zero", "zero",
    "overflow positive", "overflow negative", "max 32-bit integer", "min 32-bit integer"])
def test_reverse_working(input_value, expected_output):
    # Act
    result = Solution().reverse(input_value)
        
    # Assert
    assert result == expected_output

@pytest.mark.parametrize("input_value, expected_output", [
    # Error cases
    ("123", ValueError),
    (None, ValueError),
], ids = ["non-integer input", "None input"])
def test_reverse_exceptions(input_value, expected_output):
    # Act
    with pytest.raises(expected_output):
        Solution().reverse(input_value)