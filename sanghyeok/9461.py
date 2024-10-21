T = int(input())
for tc in range(T):
    N = int(input())

    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1



    if N <=2:
        print(1)
    else:
        for i in range(2, N):
            dp[i] = dp[i - 2] + dp[i - 3]
        print(dp[N-1])