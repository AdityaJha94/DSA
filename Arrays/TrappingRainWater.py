"""
Time Complexity: Θ(n*n)
Space Complexity: Θ(1)
"""
def trappingRainWater(arr):
    if len(arr) == 1 or len(arr) == 2:
        return 0
    res = 0
    for i in range(len(arr)):
        lMax = arr[i]
        rMax = arr[i]
        for j in range(0,i):
            lMax = max(lMax,arr[j])
        for j in range(i+1,len(arr)):
            rMax = max(rMax,arr[j])
        res += min(lMax,rMax) - arr[i]
    return res

"""
Time Complexity: Θ(n)
Space Complexity: Θ(n)
"""
def trappingRainWaterEfficient(arr):
    count = 0
    lMax = [0]*len(arr)
    rMax = [0]*len(arr)
    lMax[0] = arr[0]
    rMax[len(arr)-1] = arr[len(arr)-1]
    for i in range(1,len(arr)):
        lMax[i] = max(arr[i],lMax[i-1])
    for i in range(len(arr)-2,0,-1):
        rMax[i] = max(arr[i],rMax[i+1])
    for i in range(1,len(arr)-1):
        count += min(lMax[i],rMax[i]) - arr[i]
    return count


        
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
result = trappingRainWaterEfficient(arr)
print(result)
    
