
arr = [2,3,7]
sum = 6
n = len(arr)
memo = [[-1]*(sum+1) for i in range(n+1)]

def subsetSum(arr,sum,n):
    if sum == 0:
        return True
    if n <= 0:
        return False
    if arr[n-1] <= sum:
        return subsetSum(arr,sum-arr[n-1],n-1) or subsetSum(arr,sum,n-1)
    else:
        return subsetSum(arr,sum,n-1)

def subsetSumMemoization(arr,sum,n):
    if sum == 0:
        memo[n][sum] = True
    if n <= 0:
        memo[n][sum] = False
    if memo[n][sum] != -1:
        return memo[n][sum]
    if arr[n-1] <= sum:
        memo[n][sum] = subsetSumMemoization(arr,sum-arr[n-1],n-1) or subsetSumMemoization(arr,sum,n-1)
    else:
        memo[n][sum] = subsetSumMemoization(arr,sum,n-1)
    return memo[n][sum]
    
def subsetSumTabulation(arr,sum):
    n = len(arr)
    dp = [[False]*(sum+1) for i in range(n+1)]
    for j in range(sum+1):
        dp[0][j] = False
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                dp[i][j] = (dp[i-1][j-arr[i-1]]) or (dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]





result = subsetSumMemoization(arr,sum,n)
print(result)
