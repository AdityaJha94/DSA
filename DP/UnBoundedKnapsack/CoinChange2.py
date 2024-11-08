import sys
def coinChangeMin(coins: list[int], amount: int) -> int:
    n = len(coins)
    dp = [[-1]*(amount+1) for i in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = 0
    for j in range(amount+1):
        dp[0][j] = sys.maxsize - 1

    i = 1
    for j in range(1,amount+1):
        if j%coins[0] == 0:
            dp[i][j] = j//coins[0]
        else:
            dp[i][j] = sys.maxsize - 1

    for i in range(2,n+1):
        for j in range(1,amount+1):
            if coins[i-1] <= j:
                dp[i][j] = min(1+dp[i][j-coins[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][amount]

coins = [1]
result = coinChangeMin(coins,0)
print(result)
