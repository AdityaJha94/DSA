import sys
def mcm(arr,i,j):
    if i >= j:
        return 0
    ans = sys.maxsize
    for k in range(i,j):
        temp = mcm(arr,i,k) + mcm(arr,k+1,j) + (arr[i-1]*arr[k]*arr[j])
        if temp < ans:
            ans = temp
    return ans



t = [[-1]*1000 for i in range(1000)]
def mcmMemoization(arr,i,j):
    if i >= j:
        t[i][j] = 0
        return 0
    if t[i][j] != -1:
        return t[i][j]
    ans = sys.maxsize
    for k in range(i,j):
        temp = mcmMemoization(arr,i,k) + mcmMemoization(arr,k+1,j) + (arr[i-1]*arr[k]*arr[j])
        ans = min(ans,temp)
    t[i][j] = ans
    return ans

        

arr = [40,20,30,10,30]
result = mcmMemoization(arr,1,len(arr)-1)
print(result)
