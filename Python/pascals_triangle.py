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
        """
            Generates Pascal's triangle up to a specified number of rows.

            This function constructs Pascal's triangle, where each row represents the coefficients of the binomial expansion. 
            The triangle is built iteratively, with each element being the sum of the two elements directly above it in the previous row.

            Args:
                numRows (int): The number of rows of Pascal's triangle to generate.

            Returns:
                List[List[int]]: A list of lists representing the rows of Pascal's triangle, 
                                or an empty list if the input is invalid or less than 1.
        """
    
        # exit early if an invalid number or rows was given
        if not numRows or numRows < 1:
            return []
        
        # base cases where there are no pairs to sum
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        # prefill with n = 1 and n = 2 rows
        res = [[1], [1, 1]]
        
        # starting from 2 since 0 and 1 are already done
        for i in range(2, numRows):
            
            # get middle by summing all pairs in the previous row
            middle = [res[i-1][x] + res[i-1][x+1] for x in range(i-1)]
            
            # add the middle with 1s on both sides to the list of rows
            res.append([1] + middle + [1])
        
        # return the result
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