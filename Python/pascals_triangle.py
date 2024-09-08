"""118. Pascal's Triangle
Easy
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

Constraints:

1 <= numRows <= 30"""

import pytest
from typing import List

class Solution:
    def test(self):
        return self.generate(5)
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows or numRows < 1:
            return []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            middle = [res[i-1][x] + res[i-1][x+1] for x in range(i-1)]
            res.append([1] + middle + [1])
        
        return res
    
@pytest.mark.parametrize("numRows, expected", [
    # Happy path tests
    (1, [[1]]),
    (2, [[1], [1, 1]]),
    (3, [[1], [1, 1], [1, 2, 1]]),
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    
    # Edge cases
    (0, []),
    (10, [
        [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], 
        [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], 
        [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], 
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]),
    
    # Error cases
    (-1, []),
    (None, []),
], ids=[
        "single_row", "two_rows", "three_rows", "five_rows", 
        "zero_rows", "ten_rows", "negative_rows", "none_rows"
]
)
def test_generate(numRows, expected):
    
    # Act
    result = Solution().generate(numRows)
    
    # Assert
    assert result == expected
    
if __name__ == "__main__":
    for line in Solution().test():
        print(line)