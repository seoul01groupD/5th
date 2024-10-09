from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    direction = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


    def bfs(start, target):
        visited = [[-1] * n for _ in range(n)]
        queue = deque()
        sx, sy = start
        queue.append((sx, sy))
        visited[sx][sy] = 0

        if start == target:
            return 0

        while queue:
            tx, ty = queue.popleft()
            for dx, dy in direction:
                nx = tx + dx
                ny = ty + dy
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[tx][ty] + 1
                    queue.append((nx, ny))
                    if (nx, ny) == target:
                        return visited[nx][ny]
                    
    
    time = bfs((x1, y1), (x2, y2))
    print(time)