"""
Time Complexity:  ϴ(m*n)
"""

M = 4
N = 3

memo = [[-1]*(N+1) for i in range(M+1)]
def lcsMemoization(str1,str2,m,n):
    if memo[m][n] != -1:
        return memo[m][n]
    if m == 0 or n == 0:
        memo[m][n] = 0
    else:
        if str1[m-1] == str2[n-1]:
            memo[m][n] = 1 + lcs(str1,str2,m-1,n-1)
        else:
            memo[m][n] = max(lcs(str1,str2,m-1,n),lcs(str1,str2,m,n-1))
        
    return memo[m][n]

def lcsTabulation(str1,str2):
    m = len(str1)
    n = len(str2)
    resultStr = ""
    db = [[-1]*(n+1) for i in range(m+1)]
    for i in range(m):
        db[i][0] = 0
    for j in range(n):
        db[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                resultStr = resultStr + str1[i-1]
                db[i][j] = 1+db[i-1][j-1]
            else:
                db[i][j] = max(db[i-1][j], db[i][j-1])
    print(resultStr)
    return db[m][n]
        
"""
result = lcsMemoization("AXYZ","BAZ",M,N)
print(result)
"""

result1 = lcsTabulation("abcdaf", "acbcf")
print(result1)
