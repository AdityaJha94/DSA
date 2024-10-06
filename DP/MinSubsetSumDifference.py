def minSubsetSumDifference(arr):
    totalSum = sum(arr)
    n = len(arr)
    validSums = [0]*(totalSum//2)
    dp = [[False]*(totalSum+1) for i in range(n+1)]
    for j in range(totalSum+1):
        dp[0][j] = False
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(1,totalSum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    for k in range(0,(totalSum//2)+1):
        if dp[n][k] == True:
            validSums.append(k)
    answer = float('inf')
    for i in range(len(validSums)):
        answer = min(answer,totalSum - (2*validSums[i]))
    return answer

arr = [3,9,7,3]
result = minSubsetSumDifference(arr)
print(result)
    
