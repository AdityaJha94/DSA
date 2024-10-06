def longestSubstringWithDistinctCharacters(inputStr):
    charSet = set()
    res = 0
    l = 0
    for r in range(len(inputStr)):
        while inputStr[r] in charSet:
            charSet.remove(inputStr[l])
            l += 1
        charSet.add(inputStr[r])
        res = max(res,r-l+1)
    return res

inputStr = 'abcdabc'
result = longestSubstringWithDistinctCharacters(inputStr)
print(result)
                   
