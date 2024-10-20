n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))