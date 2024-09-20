import heapq
def djikstra_traverse(matrix, source, target):
    m, n = len(matrix), len(matrix[0])
    
    if not (is_valid(source, m, n) and is_valid(target, m, n)): return -1
    if source == target: return 0
    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    s_x, s_y = source
    dist[s_x][s_y] = 0
    t_x, t_y = target
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, s_x, s_y))

    while q:
        distance, x, y = heapq.heappop(q)
        if (x, y) == (t_x, t_y): return distance
        for dx, dy in directions:
            newx, newy = x+dx, y+dy
            if is_valid((newx, newy), m, n):
                new_dist = distance + matrix[newx][newy]
                if new_dist < dist[newx][newy]:
                    dist[newx][newy] = new_dist
                    heapq.heappush(q, (new_dist, newx, newy))
    return -1
                

def is_valid(point, m, n):
    return 0 <= point[0] < m and 0 <= point[1] < n

if __name__ == "__main__":
    matrix = [[0, 1, 10, 10],
              [10, 1, 1, 10],
              [10, 10, 1, 1],
              [10, 10, 10, 1]]
    res = djikstra_traverse(matrix, (0, 0), (3, 3))
    print(res)
    