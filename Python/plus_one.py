"""66. Plus One
Easy
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.plusOne([1, 2, 3])
    
    def plusOne(self, digits: List[int]) -> List[int]:
        """
            Increments a number represented as an array of digits by one.

            This function takes a list of integers where each integer represents a single digit of a number, 
            and adds one to the number. It handles carrying over when digits exceed 9 and returns the updated list of digits.

            Args:
                digits (List[int]): A list of integers representing the digits of the number.

            Returns:
                List[int]: The list of integers representing the digits of the incremented number.
        """
        # start at rightmost digit
        for i in range(len(digits)-1, -1, -1):

            # if no carrying needs to be done, return the result with 1 added
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # carrying will need to be done, set the current to 0 and iterate, as that add 1 to the next position anyways
            digits[i] = 0

        # if it doesn't return by the end of iteration, final carry needs to be done, so insert a 1 at the beginning of the list and return
        digits.insert(0, 1)
        return digits
    
@pytest.mark.parametrize(
    "digits, expected",
    [
        # Happy path tests
        ([1, 2, 3], [1, 2, 4]),  # simple increment
        ([9, 9, 9], [1, 0, 0, 0]),  # carry over all digits
        ([0], [1]),  # single zero

        # Edge cases
        ([1, 0, 0, 0], [1, 0, 0, 1]),  # leading zeros
        ([9], [1, 0]),  # single nine
        ([2, 9, 9], [3, 0, 0]),  # carry over last two digits

        # Error cases
        ([], [1]),  # empty list
    ],
    ids=[
        "simple_increment",
        "carry_over_all_digits",
        "single_zero",
        "leading_zeros",
        "single_nine",
        "carry_over_last_two_digits",
        "empty_list",
    ]
)
def test_plusOne(digits, expected):
    # Act
    result = Solution().plusOne(digits)

    # Assert
    assert result == expected
    
if __name__ == "__main__":
    print(Solution().test())