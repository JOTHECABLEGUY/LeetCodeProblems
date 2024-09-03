"""9. Palindrome Number
Easy
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?"""

import math
import pytest
from functools import lru_cache
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Determines if an integer is a palindrome.

            This function checks whether the given integer reads the same backward as forward. 
            It converts the integer to a string, processes it, and compares the characters to 
            determine if it is a palindrome.

            Args:
                x (int): The integer to be checked for palindrome properties.

            Returns:
                bool: True if the integer is a palindrome, False otherwise.
        """
        if not isinstance(x, int):
            return False
        s = '#'.join(str(x))
        if len(s) in {2, 1}:
            return True
        if len(s) == 3:
            return s[0] == s[-1]
        mid_ind = len(s)//2
        return s[:mid_ind] == s[:mid_ind:-1]
    @lru_cache()
    def isPalindrome_2(self, x: int) -> bool:
        """Determines if an integer is a palindrome.

            This function checks whether the given integer reads the same backward as forward. 
            It converts the integer to a string, processes it, and compares the characters to 
            determine if it is a palindrome.

            Args:
                x (int): The integer to be checked for palindrome properties.

            Returns:
                bool: True if the integer is a palindrome, False otherwise.
        """
        # not a palindromic number if input is not an int
        if not isinstance(x, int):
            return False

        # negative sign will invalidate
        if x < 0:
            return False
        
        # number of digits in the number (if x == 0 then there is 1 digit)
        num_digits = int(math.log10(x)) + 1 if x else 1
        
        # all single digit numbers are palindromes
        if num_digits == 1:
            return True
        
        # 2 digit numbers are palindromes if the left == right
        if num_digits == 2:
            left, right = divmod(x, 10)
            return left == right
        
        # for longer numbers, start on the outside and work towards the middle.
        #   If any pair of mirrored digits are different, the number is not a palindrome,
        #   otherwise it is a palindrome.
        return all(
            self.get_leftmost_digit(x, num_digits, index)
            == self.get_rightmost_digit(x, index)
            for index in range(num_digits // 2)
        )
    
    def get_leftmost_digit(self, x:int, num_digits:int, index:int) -> int:
        """
            Retrieves the leftmost digit of a number at a specified index.

            This function calculates the leftmost digit of a given integer based on the 
            number of digits and the specified index. It returns the digit at the 
            specified position from the left, or 0 if the input number is zero.

            Args:
                x (int): The integer from which to extract the leftmost digit.
                num_digits (int): The total number of digits in the integer.
                index (int): The index of the digit to retrieve, starting from 0.

            Returns:
                int: The leftmost digit at the specified index, or 0 if the input number is zero.
        """
        return (x//pow(10, num_digits-index-1))%10 if x else 0
    
    def get_rightmost_digit(self, x:int, index:int) -> int:
        """
            Retrieves the rightmost digit of a number at a specified index.

            This function extracts the digit from the right side of a given integer based 
            on the specified index. It returns the digit at the specified position from the 
            right, or 0 if the input number is zero.

            Args:
                x (int): The integer from which to extract the rightmost digit.
                index (int): The index of the digit to retrieve, starting from 0.

            Returns:
                int: The rightmost digit at the specified index, or 0 if the input number is zero.
        """
        return (x%int(pow(10, index + 1)))//pow(10, index)
    def test(self):
        return self.isPalindrome_2(100010001)

@pytest.mark.parametrize("x, expected", [
    # Happy path tests
    (121, True),
    (-121, False),
    (10, False),
    (0, True),
    (1, True),
    (12321, True),
    (1221, True),
    # Edge cases
    (123456789987654321, True),
    (123456789987654320, False),
    # Error cases
    (None, False),
    ("121", False),
    (12.21, False),
], ids=["positive_palindrome", "negative_number", "non_palindrome", "single_digit_zero", "single_digit_one", "odd_length_palindrome"
        , "even_length_palindrome", "large_palindrome", "large_non_palindrome", "none_input", "string_input", "float_input"])
def test_isPalindrome(x, expected):
    
    # Act
    result = Solution().isPalindrome(x)
    
    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())