def longestEvenOddSub(arr):
    maxCount = 1
    count = 1
    for i in range(1,len(arr)):
        if (arr[i-1]%2 == 0 and arr[i]%2 != 0) or (arr[i-1]%2 != 0 and arr[i]%2 == 0):
            count += 1
            maxCount = max(maxCount,count)
        else:
            count = 1
    return maxCount

arr = [5,10,20,6,3,8]
res = longestEvenOddSub(arr)
print(res)
