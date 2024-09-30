n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
# lst.sort()

dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, k + 1):
        weight, value = lst[i - 1]
        if weight > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

print(dp[-1][-1])