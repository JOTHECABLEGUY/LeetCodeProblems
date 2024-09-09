"""119. Pascal's Triangle II
Easy
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]

Constraints:

0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.getRow(1)
    
    def getRow(self, rowIndex: int) -> List[int]:
        """
            Generates the specified row of Pascal's triangle.

            This function computes the row at the given index in Pascal's triangle, where each element is the sum of the two elements directly above it. 
            The function handles invalid indices gracefully and returns an empty list for such cases.

            Args:
                rowIndex (int): The index of the row in Pascal's triangle to generate.

            Returns:
                List[int]: A list of integers representing the specified row of Pascal's triangle, 
                            or an empty list if the rowIndex is invalid.
        """
        
        # exit early if invalid row index is given
        if rowIndex is None or rowIndex < 0:
            return []
        
        # base cases, where there aren't any previous pairs to sum
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        # pre fill previous row with first valid pair in the triangle
        prev_row = [1, 1]
        
        # for each row until we hit the requested row, sum the pairs in the previous row 
        #   and add 1s to both sides, the new row is now the most recent
        for i in range(2, rowIndex + 1):
            middle = [prev_row[x] + prev_row[x+1] for x in range(i-1)]
            prev_row = [1] + middle + [1]
            
        # the most recent row after the stopIteration will be the row at the requested index
        return prev_row
    
@pytest.mark.parametrize("rowIndex, expected", [
    # Happy path tests
    (0, [1]),  # ID: single element
    (1, [1, 1]),  # ID: two elements
    (2, [1, 2, 1]),  # ID: three elements
    (3, [1, 3, 3, 1]),  # ID: four elements
    (4, [1, 4, 6, 4, 1]),  # ID: five elements

    # Edge cases
    (-1, []),  # ID: negative index
    (None, []),  # ID: None index

    # Larger values
    (10, [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]),  # ID: larger row
], ids = [
    "single element", "two elements", "three elements", "four elements", "five elements", "negative index", "None index", "larger row"
])
def test_getRow(rowIndex, expected):
    # Act
    result = Solution().getRow(rowIndex)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())