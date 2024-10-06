"""
Time Complexity: θ(n)
Recurrence Relation: T(n) = T(n-2) + θ(1)
Auxiliary Space: θ(n/2)
"""
def isPalindrome(inputStr,start,end):
    if start >= end:
        return True
    return inputStr[start] == inputStr[end] and isPalindrome(inputStr,start+1,end-1)


result = isPalindrome("acbca",0,4)
print(result)
