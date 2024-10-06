def longestCommonSubstring(str1,str2,m,n):
    db = [[-1]*(n+1) for i in range(m+1)]
    result = 0
    for i in range(m):
        db[i][0] = 0
    for j in range(n):
        db[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1] == str2[j-1]:
                db[i][j] = 1 + db[i-1][j-1]
                result = max(result,db[i][j])
            else:
                db[i][j] = 0
    return result

str1 = "gheabcdz"
str2 = "abdef"
result = longestCommonSubstring(str1,str2,len(str1),len(str2))
print(result)
