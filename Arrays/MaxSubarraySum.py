"""
Time Complexity: Θ(n*n)
Space Complexity: Θ(1)
"""
def maxSubrraySum(arr):
    res = arr[0]
    for i in range(len(arr)):
        count = 0
        for j in range(i,len(arr)):
            count += arr[j]
            res = max(res,count)
    return res

"""
Time Complexity: Θ(n)
Space Complexity: Θ(1)
"""
def maxSubArraySumEfficient(arr):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1,len(arr)):
        maxEnding = max(maxEnding+arr[i],arr[i])
        res = max(maxEnding,res)
    return res

arr = [-2,1,-3,4,-1,2,1,-5,4]
result = maxSubArraySumEfficient(arr)
print(result)
