"""2220. Minimum Bit Flips to Convert Number
Easy
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.


Example 1:

Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.
Example 2:

Input: start = 3, goal = 4
Output: 3
Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 011 -> 010.
- Flip the second bit from the right: 010 -> 000.
- Flip the third bit from the right: 000 -> 100.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.

Constraints:

0 <= start, goal <= 109"""

import pytest
from operator import xor

class Solution:
    
    def test(self):
        return self.minBitFlips(-2, 1)
    
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start^goal).count('1')

@pytest.mark.parametrize(
    "start, goal, expected",
    [
        # Happy path tests
        (10, 20, 4),  # Different bits in binary representation
        (0, 0, 0),    # No flips needed
        (1, 2, 2),    # Single bit difference

        # Edge cases
        (0, 1, 1),    # Smallest non-zero flip
        (2**31-1, 0, 31),  # Maximum 32-bit integer to zero
        (0, 2**31-1, 31),  # Zero to maximum 32-bit integer

        # Error cases
        (-1, 1, 32),  # Negative number to positive
        (1, -1, 32),  # Positive number to negative
    ],
    ids=[
        "happy_path_10_to_20",
        "happy_path_0_to_0",
        "happy_path_1_to_2",
        "edge_case_0_to_1",
        "edge_case_max_int_to_0",
        "edge_case_0_to_max_int",
        "error_case_neg1_to_1",
        "error_case_1_to_neg1",
    ]
)
def test_minBitFlips(start, goal, expected):

    # Act
    result = Solution().minBitFlips(start, goal)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())