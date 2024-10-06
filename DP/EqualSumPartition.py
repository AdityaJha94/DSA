
def equalSumPartition(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    if sum%2 != 0:
        return False
    targetSum = sum//2
    print(targetSum)
    return subsetSumTabulation(arr,targetSum)

    
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

arr = [2,3,7]
result = equalSumPartition(arr)
print(result)
