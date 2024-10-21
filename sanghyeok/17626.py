import sys

input = sys.stdin.readline


def min_four_squares(N):
    square = []
    i = 1
    while True:
        if i*i>N:
            break
        else:
            square.append(i*i)
            i+=1

    dp = [50001]*(N+1)
    dp[0] = 0

    for k in square:
        for j in range(k, N+1):
            dp[j] = min(dp[j], dp[j-k]+1)

    return dp[N]



N = int(input())
result = min_four_squares(N)
print(result)
# dp = [0, 1]
# for i in range(2, N+1):
#     min_value = 4
#     j = 1
#     while (j**2) <= i:
#         min_value = min(min_value, dp[i-j**2])
#         j += 1
#     dp.append(min_value + 1)
# print(dp[N])

