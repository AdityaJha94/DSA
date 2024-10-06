def peakElementIndex(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == len(arr)-1 or
                                                     arr[mid+1] <= arr[mid]):
            return mid
        if mid > 0 and arr[mid-1] >= arr[mid]:
            high = mid - 1
        else:
            low = mid+1
    return -1

def binSearch(arr,K):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        print(mid)
        if arr[mid] == K:
            return 1
        elif arr[mid] > K:
            high = mid-1
        else:
            low = mid+1
    return -1

def testMaxElement(arr):
    temp = [0]*(max(arr)+1)
    for i in range(len(arr)):
        temp[arr[i]] += 1
    maxInTemp = max(temp)
    if maxInTemp > len(arr)//2:
        return temp.index(maxInTemp)
    return -1

arr2 = [15]
result2 = testMaxElement(arr2)
print(result2)

"""
arr1 = [1,2,3,4,6]
result1 = binSearch(arr1,6)
print(result1)
"""

"""
arr = [1,2,1,3,5,6,4]
result = peakElementIndex(arr)
print(result)
"""

                                                     
                                                     
                                                     
