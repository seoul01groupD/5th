from collections import deque
from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

chicken = []; house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])

chicken_dist = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(start):
    queue = deque(start)
    visited = [[-1] * n for _ in range(n)]
    for x, y in start:
        visited[x][y] = 0

    while queue:
        tx, ty = queue.popleft()
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[tx][ty] + 1
                queue.append([nx, ny])
    
    return visited
                
min_dist = 1e9

for chosen in combinations(chicken, m):
    distance = bfs(chosen)
    total_dist = 0
    for hx, hy in house:
        total_dist += distance[hx][hy]
    min_dist = min(min_dist, total_dist)

print(min_dist)