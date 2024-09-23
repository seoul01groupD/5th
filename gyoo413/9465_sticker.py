T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0, 0, 0] for _ in range(n)]
    
    dp[0] = [0, sticker[0][0], sticker[1][0]]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = sticker[0][i] + max(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = sticker[1][i] + max(dp[i - 1][0], dp[i - 1][1])
        
    result = max(dp[-1])
    print(result)