/*
463. Island Perimeter
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
There is exactly one island in grid.
 */

class Solution {

    /**
     * Method to find the perimeter of square cells of land arranged within a grid
     * @param grid (int[][]): matrix of dimensions r x c where r is the number of rows, c is the number of columns, and each
     *                          cell represents a 1x1 unit of land if the value is 1, water if 0
     * @return int: perimeter of the landmass present in the grid
     */
    public int islandPerimeter(int[][] grid) {

        // init perimeter, num of rows, and num of columns
        int perim = 0;
        int rows = grid.length;
        int cols = grid[0].length;

        // each land cell has at most 4 sides that contribute to the entire landmass's perimeter
        int exposed_sides = 4;

        // traverse the grid
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){

                // continue if the current cell is water
                if (grid[i][j] == 0) continue;

                // remove an exposed side if the cell to the north is land
                if (i != 0 && grid[i-1][j] == 1) exposed_sides--;

                // remove an exposed side if the cell to the south is land
                if (i < rows-1 && grid[i+1][j] == 1) exposed_sides--;

                // remove an exposed side if the cell to the west is land
                if (j != 0 && grid[i][j-1] == 1) exposed_sides--;

                // remove an exposed side if the cell to the east is land
                if (j < cols-1 && grid[i][j+1] == 1) exposed_sides--;

                // add the number of exposed sides for the current cell to the perimeter
                perim += exposed_sides;

                // reset exposed sides for the next land cell
                exposed_sides = 4;
            }
        }

        // return the resulting perimeter
        return perim;
    }
    public static void main(String[] args) {
        Solution obj = new Solution();
        int[][] grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
        System.out.println(obj.islandPerimeter(grid));
    }
}
