def maxConsecutiveOne(arr):
    count = 0
    maxCount = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        maxCount = max(count,maxCount)
    return maxCount

arr = [1]
res = maxConsecutiveOne(arr)
print(res)
