import java.util.PriorityQueue;
class Dijkstra {
    private final int[][] directions = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    public int traverse(int[][] matrix, int[] source, int[] target){
        int m = matrix.length;
        if (m < 1) return -1;
        int n = matrix[0].length;
        if (n < 1) return -1;
        int s_x = source[0], s_y = source[1];
        int t_x = target[0], t_y = target[1];
        if (s_x == t_x && s_y == t_y) return -1;
        if (!isValid(source, m, n) || !isValid(target, m, n)) return 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[2], b[2]));
        int[][] dist = new int[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                dist[i][j] = Integer.MAX_VALUE;
            }
        }
        dist[source[0]][source[1]] = 0;

        heap.add(new int[]{source[0], source[1], 0});

        while (!heap.isEmpty()){
            int[] node = heap.poll();
            int x = node[0], y = node[1], distance = node[2];
            if (x == t_x && y == t_y) return distance;
            for (int[] dir : directions){
                int[] new_point = new int[]{x+ dir[0], y + dir[1]};
                if (isValid(new_point, m, n) && distance + matrix[new_point[0]][new_point[1]] < dist[new_point[0]][new_point[1]]){
                    dist[new_point[0]][new_point[1]] = distance + matrix[new_point[0]][new_point[1]];
                    heap.add(new int[]{new_point[0], new_point[1], dist[new_point[0]][new_point[1]]});
                    }
                }
            }
        return -1;
    }
    
    private boolean isValid(int[] point, int m, int n){
        return point[0] < m && point[0] >- 1 && point[1] > -1 && point[1] < n;
    }

    public static void main(String[] args){
        int[][] matrix = new int[][]{{1, 1, 1, 1, 10},
                                    {1, 1, 1, 3, 1},
                                    {1, 1, 3, 1, 1},
                                    {1, 3, 1, 1, 1},
                                    {3, 1, 1, 1, 1}};
        int[] source = new int[]{0, 0};
        int[] target = new int[]{4, 4};
        Dijkstra d = new Dijkstra();
        System.out.println(d.traverse(matrix, source, target));
    }
}
