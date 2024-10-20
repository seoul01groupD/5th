n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
diff = 1e9


def backtracking(level, start):
    global n, diff

    if level == n // 2:
        stat1 = 0; stat2 = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if visited[i] == 1 and visited[j] == 1:
                    stat1 += (stat[i][j] + stat[j][i])
                elif visited[i] == 0 and visited[j] == 0:
                    stat2 += (stat[i][j] + stat[j][i])
        diff = min(diff, abs(stat1 - stat2))
        return
    
    for w in range(start, n):
        if visited[w] == 0:
            visited[w] = 1
            backtracking(level + 1, w + 1)
            visited[w] = 0


backtracking(0, 0)
print(diff)