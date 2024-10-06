
W = 3
n = 3
weight = [4,5,1]
val = [1,2,3]
memo = [[-1]*(W+1) for i in range(n+1)]

def knapsackRecursive(weight,val,W,n):
    if n == 0 or W == 0:
        return 0
    if W >= weight[n-1]:
        return max(val[n-1] + knapsackRecursive(weight,val,W-weight[n-1],n-1),
                   knapsackRecursive(weight,val,W,n-1))
    elif W < weight[n-1]:
        return knapsackRecursive(weight,val,W,n-1)




def knapsackMemoization(weight,val,W,n):
    if n == 0 or W == 0:
        memo[n][W] = 0
    if memo[n][W] != -1:
        return memo[n][W]
    if W >= weight[n-1]:
        memo[n][W] = max(val[n-1] + knapsackRecursive(weight,val,W-weight[n-1],n-1),
                   knapsackRecursive(weight,val,W,n-1))
    elif W < weight[n-1]:
        memo[n][W] = knapsackRecursive(weight,val,W,n-1)
    return memo[n][W]

def knapsackTabulation(weight,val,W,n):
    dp = [[-1]*(W+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for j in range(W+1):
        dp[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if weight[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j - weight[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][W]

result = knapsackMemoization(weight,val,W,n)
print(result)

