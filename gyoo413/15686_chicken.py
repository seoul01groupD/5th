from collections import deque, combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

chicken = []; house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])

c = len(chicken)
h = len(house)

chicken_dist = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(start, target):
    queue = deque()
    sx = start[0]; sy = start[1]
    queue.append([sx, sy])
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1

    while queue:
        tx, ty = queue.popleft()
        for k in range(4):
            nx = tx + dx[k]
            ny = ty + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = visited[tx][ty] + 1
                queue.append([nx, ny])
                if [nx, ny] == target:
                    return visited[nx][ny] - 1
                
for home in house:
    temp = []
    for chick in chicken:
        dist = bfs(home, chick)
        temp.append(dist)
    chicken_dist.append(temp)

min_dist = 1e9
visited = [0] * c
def backtracking(level):
    global m, c, h, min_dist

    if level == m:
        temp_dist = 0
        for j in range(h):
            temp = []
            for k in range(c):
                if visited[k] == 1:
                    temp.append(chicken_dist[j][k])
            temp_dist += min(temp)
            if temp_dist > min_dist:
                return
        min_dist = temp_dist
        return 
    
    for i in range(c):
        if visited[i] == 0:
            visited[i] = 1
            backtracking(level + 1)
            visited[i] = 0

backtracking(0)

print(min_dist)
