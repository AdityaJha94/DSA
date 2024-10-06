def lexicographicRank(inputStr):
    n = len(inputStr)
    res = 1
    countArr = [0]*256
    for i in range(n):
        countArr[ord(inputStr[i]) - ord('a')] += 1
    fact = [0]*n
    fact[0] = 1
    fact[1] = 1
    for i in range(2,n):
        fact[i] = fact[i-1]*i
    for i in range(n):
        count = 0
        for j in range(ord(inputStr[i]) - ord('a')):
            count += countArr[j]
        countArr[ord(inputStr[i]) - ord('a')] -= 1
        res += (count*fact[n-1-i])
    return res


inputStr = 'dcba'
result = lexicographicRank(inputStr)
print(result)
