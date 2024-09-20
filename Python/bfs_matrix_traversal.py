from collections import deque
def bfs_traverse(matrix, start, stop):
    sx, sy = start
    ex, ey = stop
    if ex == sx and ey == sy: return 0
    q = deque([(sx, sy, 0)])
    
    while q:
        x, y, dist = q.popleft()
        if (x, y) == (ex, ey):
            return dist
        matrix[x][y] = 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newx, newy = x+dx, y+dy
            if isValid((newx, newy), matrix):
                q.append((newx, newy, dist+1))
    return -1
    
def isValid(point, matrix):
    return 0 <= point[1] < len(matrix) and 0 <= point[0] < len(matrix[0]) and not matrix[point[1]][point[0]]

if __name__ == "__main__":
    matrix = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    res = bfs_traverse(matrix, (0, 0), (3, 3))
    print(res)
    