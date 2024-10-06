"""
Time Complexity: Θ(n*n)
Space Complexity: Θ(1)
"""
def maxDifference(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] - arr[i] > max:
                max = arr[j] - arr[i]
    return max


"""
Time Complexity: Θ(n)
Space Complexity: Θ(1)
"""
def maxDifferenceEfficient(arr):
    result = arr[1] - arr[0]
    minValue = arr[0]
    for j in range(1,len(arr)):
        result = max(result,arr[j]-minValue)
        minValue = min(minValue,arr[j])
    return result

arr = [2,3,10,6,4,8,1]
result = maxDifferenceEfficient(arr)
print(result)
