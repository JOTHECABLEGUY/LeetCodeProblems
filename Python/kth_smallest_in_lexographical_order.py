"""440. K-th Smallest in Lexicographical Order
Hard
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].


Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1

Constraints:

1 <= k <= n <= 109"""

import pytest

class Solution:
    
    def test(self): return (self.findKthNumber(50, 20))
    
    def findKthNumber(self, n: int, k: int) -> int:
        """
            Find the k-th smallest number in lexicographical order among the numbers from 1 to n.

            This function determines the k-th smallest integer when the integers from 1 to n are sorted in 
            lexicographical order. It efficiently navigates through the number space to find the desired 
            k-th number without generating all numbers explicitly.

            Args:
                n (int): The upper limit of the range (1 to n).
                k (int): The position in the lexicographical order to find.

            Returns:
                int: The k-th smallest number in lexicographical order.
        """
        if k <= 0 or n <= 0: return 0
        current = 1
        k -= 1
        while k > 0:
            count = self.count_steps(n, current, current + 1)
            if count <= k:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1
        return current
    
    def count_steps(self, n, start, stop):
        """
            Count the number of integers in the range [start, stop) that are less than or equal to n.

            This function calculates how many numbers exist between the specified start and stop values, 
            considering the upper limit n. It iteratively expands the range by multiplying the start and 
            stop values by 10, effectively counting numbers in each "digit level" until the start exceeds n.

            Args:
                n (int): The upper limit for counting.
                start (int): The starting number of the range.
                stop (int): The stopping number of the range (exclusive).

            Returns:
                int: The total count of integers in the range [start, stop) that are less than or equal to n.
        """
        steps = 0
        while start <= n:
            steps += min(n+1, stop) - start
            start *= 10
            stop *= 10
        return steps

@pytest.mark.parametrize(
    "n, k, expected",
    [
        # Happy path tests
        (13, 2, 10),  # ID: happy_path_1
        (100, 10, 17),  # ID: happy_path_2
        (50, 20, 27),  # ID: happy_path_3

        # Edge cases
        (1, 1, 1),  # ID: edge_case_1
        (10, 10, 9),  # ID: edge_case_2
        (1000000000, 1000000000, 999999999),  # ID: edge_case_3

        # Error cases
        (0, 1, 0),  # ID: error_case_1
        (10, 0, 0),  # ID: error_case_2
        (-1, 1, 0),  # ID: error_case_3
    ],
    ids=[
        "happy_path_1", "happy_path_2", "happy_path_3",
        "edge_case_1", "edge_case_2", "edge_case_3",
        "error_case_1", "error_case_2", "error_case_3"
    ]
)
def test_findKthNumber(n, k, expected):
    # Act
    result = Solution().findKthNumber(n, k)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())