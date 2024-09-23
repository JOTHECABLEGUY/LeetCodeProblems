import java.util.*;
public class find_islands {
    private final static int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int numislands(int[][] matrix){
        int m = matrix.length;
        if (m < 1) return 0;
        int n = matrix[0].length;
        if (n < 1) return 0;
        int islands = 0;

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (matrix[i][j] == 1){
                    process_island(matrix, i, j);
                    islands++;
                }
            }
        }
        return islands;
    }
    private void process_island(int[][] matrix, int i, int j){
        Queue<int[]> pq = new LinkedList<>();
        pq.add(new int[]{i, j});
        while (!pq.isEmpty()){
            int[] cell = pq.poll();
            matrix[cell[0]][cell[1]] = 0;
            for (int[] d : directions){
                int newx = cell[0] + d[0], newy = cell[1] + d[1];
                if (isValid(newx, matrix.length, newy, matrix[0].length) && matrix[newx][newy] == 1) pq.add(new int[]{newx, newy});
            }
        }
    }

    private boolean isValid(int i, int m, int j, int n){
        return i > -1 && i < m && j > -1 && j < n;
    }

    public static void main(String[] args) {
        find_islands solution = new find_islands();
        
        // Example grid
        int[][] grid = {
            {1, 1, 0, 0, 0},
            {1, 1, 0, 0, 0},
            {0, 0, 1, 0, 0},
            {0, 0, 0, 1, 1}
        };
        
        int result = solution.numislands(grid);
        System.out.println("Number of islands: " + result); // Output: 3
    }
}
