n = int(input())
counsel = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 6)
for cur in range(n):
    day, pay = counsel[cur]
    finish = cur + day
    if finish <= n + 5:
        dp[finish] = max(dp[finish], dp[cur] + pay)
    dp[cur + 1] = max(dp[cur + 1], dp[cur])

result = max(dp[:n + 1])

print(result)
