"""
Time Complexity: O(n*log(sum-max))
"""

def allocateMinPages(arr,k):
    sum = 0
    maximum = arr[0]
    for i in range(len(arr)):
        sum += arr[i]
        maximum = max(maximum,arr[i])
    low = maximum
    high = sum
    res = 0
    while low <= high:
        mid = (low+high)//2
        if isFeasible(arr,k,mid):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res


def isFeasible(arr,k,ans):
    req = 1
    sum = 0
    for i in range(len(arr)):
        if (sum+arr[i]) > ans:
            req += 1
            sum = arr[i]
        else:
            sum += arr[i]
    return (req <= k)
    
        
arr = [10,20,10,30]
result = allocateMinPages(arr,2)
print(result)
