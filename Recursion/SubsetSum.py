"""
Time Complexity = θ(2^n)
"""
def subsetSum(arr,n,sum):
    if n == 0:
        return 1 if sum == 0 else 0
        
    return subsetSum(arr,n-1,sum) + subsetSum(arr,n-1,sum-arr[n-1])

arr = [10,15,20]
result = subsetSum(arr,3,25)
print(result)
    
