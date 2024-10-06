import sys
def leftmostNonRepeating(inputStr):
    fIndex = [-1]*256
    res = sys.maxsize
    for i in range(len(inputStr)):
        fi = fIndex[ord(inputStr[i])-ord('a')]
        if fi == -1:
            fIndex[ord(inputStr[i])-ord('a')] = i
        else:
            fIndex[ord(inputStr[i])-ord('a')] = -2
    for i in range(len(fIndex)):
        if fIndex[i] >= 0:
            res = min(res,fIndex[i])
    return -1 if res == sys.maxsize else res

inputStr = 'abbcbda'
result = leftmostNonRepeating(inputStr)
print(result)
            
