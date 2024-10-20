import sys
input = sys.stdin.readline
        
n = int(input())
lst = list(map(int, input().split()))

dp_right = [0] * n
dp_left = [0] * n

for i in range(n):
    dp_right[i] = 1
    dp_left[i] = 1  
    for j in range(i):
        if lst[j] < lst[i]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)
for i in range(n - 1, -1, -1):
    for k in range(i + 1, n):
        if lst[k] < lst[i]:
            dp_left[i] = max(dp_left[i], dp_left[k] + 1)

dp = [0] * n
for i in range(n):
    dp[i] = dp_right[i] + dp_left[i] -1

print(max(dp))
