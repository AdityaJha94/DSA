def printLCS(str1,str2):
    m = len(str1)
    n = len(str2)
    resultStr = ""
    dp = [[-1]*(n+1) for i in range(m+1)]
    for i in range(m):
        dp[i][0] = 0
    for j in range(n):
        dp[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            resultStr = resultStr + str1[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i = i-1
            else:
                j = j-1
    resultStr = resultStr[::-1]
    return resultStr

str1 = "abcdaf"
str2 = "acbcf"
result = printLCS(str1,str2)
print(result)
