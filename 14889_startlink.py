def dfs(s, cnt):
    global team, n

    if cnt == n // 2:
        start.append(team)
        start_visited.append(visited.copy())
        return
    
    visited[s] = 1

    for w in range(n):
        if visited[w] == 0:
            visited[w] = 1
            team += stat[s][w]
            team += stat[w][s]
            dfs(w, cnt + 1)
            team -= stat[s][w]
            team -= stat[w][s]
            visited[w] = 0


n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    visited = [0] * n
    team = 0
    start_visited = []
    start = []
    dfs(i, 1)

    print(start, start_visited)
