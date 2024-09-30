from collections import deque

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

print(chicken_dist)

minimum_chicken_dist = 1e9

# def backtracking(level, dist_sum):
#     global m, minimum_chicken_dist

#     if level == m:
#         return
    
#     if dist_sum > minimum_chicken_dist:
#         return
        
#     for i in range(len(chicken_dist)):
#         for j in range()