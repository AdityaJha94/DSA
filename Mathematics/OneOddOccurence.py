"""
Time Complexity: Θ(n)
Space Complexity: Θ(1)
"""

def getOneOddOccurenceNumber(arr):
    res = arr[0]
    for i in range(1,len(arr)):
        res = res ^ arr[i]

    return res

input = [5,6,7,6,7,8,8]
result = getOneOddOccurenceNumber(input)
print(result)

result1 = 5<<2
print(result1)
