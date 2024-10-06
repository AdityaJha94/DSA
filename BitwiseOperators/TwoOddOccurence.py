"""
Time Complexity: Θ(n)
Space Complexity: Θ(1)
"""

def twoOddOccuringNumber(arr):
    x = arr[0]
    for i in range(1,len(arr)):
        x = x ^ arr[i]
    k = x&(~(x-1))
    res1 = 0
    res2 = 0
    for i in range(0,len(arr)):
        if (arr[i]&k) != 0:
            res1 ^= arr[i]
        else:
            res2 ^= arr[i]
    print(res1)
    print(res2)

input = [5,6,7,6,7,8,8,9,9,9,10,10]
result = twoOddOccuringNumber(input)
