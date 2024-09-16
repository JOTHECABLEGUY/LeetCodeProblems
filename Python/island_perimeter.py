"""463. Island Perimeter
Easy
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid."""

import itertools
import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
            Calculate the perimeter of an island represented in a grid.

            This function takes a 2D grid where 1s represent land and 0s represent water, 
            and computes the total perimeter of the island formed by the land cells. 
            The perimeter is defined as the number of edges of land cells that are not 
            adjacent to other land cells.

            Args:
                grid (List[List[int]]): A 2D list representing the grid of land and water.

            Returns:
                int: The perimeter of the island. Returns 0 if the grid is empty or contains no land.
        """
        
        # return early if there are no cells to process
        if not (grid and grid[0]):
            return 0
        
        # store the accumulated perimeter
        perim = 0
        
        # traverse the grid using the product of ranges
        for i, j in itertools.product(range(len(grid)), range(len(grid[0]))):
            
            # continue if water
            if not grid[i][j]: continue
            
            # add 4 to perimeter and take 2 away if land to the left or above,
            #   if there is land below or to the right, future iterations will 
            #   adjust the perimeter
            perim += 4
            if i > 0 and grid[i-1][j]: perim -= 2
            if j > 0 and grid[i][j-1]: perim -= 2
        
        # return perimeter of landmass
        return perim

@pytest.mark.parametrize("grid, expected, _id", [
    # Happy path tests
    ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 16, "happy_path_1"),
    ([[1]], 4, "happy_path_2"),
    ([[1,0]], 4, "happy_path_3"),
    
    # Edge cases
    ([], 0, "empty_grid"),
    ([[0]], 0, "single_zero"),
    ([[1,1],[1,1]], 8, "small_square"),
])
def test_island_perimeter(grid, expected, _id):
    # Act
    result = Solution().islandPerimeter(grid)

    # Assert
    assert result == expected, f"Failed on {_id}"

if __name__ == "__main__":
    print(Solution().test())