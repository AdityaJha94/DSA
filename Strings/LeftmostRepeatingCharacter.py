import sys
def leftmostRepeatingChar(inputStr):
    count = [-1]*256
    for i in range(len(inputStr)):
        count[ord(inputStr[i]) - ord('a')] += 1
    for i in range(len(inputStr)):
        if count[ord(inputStr[i]) - ord('a')] > 1:
            return i
    return -1

def leftmostRepeatingCharOneLoop(inputStr):
    firstIndex = [-1]*256
    res = sys.maxsize
    for i in range(len(inputStr)):
        fi = firstIndex[ord(inputStr[i])-ord('a')]
        if fi == -1:
            firstIndex[ord(inputStr[i])-ord('a')] = i
        else:
            res = min(res,fi)
    return -1 if res == sys.maxsize else res
            

inputStr = 'abccbd'
result = leftmostRepeatingCharOneLoop(inputStr)
print(result)
