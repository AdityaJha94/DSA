def rodCutting(n,prices):
    length = []
    for i in range(1,n+1):
        length.append(i)
    W = len(length)
    dp = [[-1]*(W+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(W+1):
        dp[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if length[i-1] <= j:
                dp[i][j] = max(prices[i-1] + dp[i][j-length[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]


lengthOfRod = 8
prices = [1,5,8,9,10,17,17,20]
result = rodCutting(lengthOfRod,prices)
print(result)
