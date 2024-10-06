def countOccurrences(arr,k):
    temp = {}
    count = 0
    for n in arr:
        temp[n] = 1 + temp.get(n,0)
    for key,value in temp.items():
        if value > len(arr)//k:
            count += 1
    return count

arr = [3,1,2,2,1,2,3,3]
result = countOccurrences(arr,4)
#print(result)


def minInRotatedSorted(arr,low,high):
    res = arr[0]
    while low <= high:
        if arr[low] < arr[high]:
            res = min(res,arr[low])
            break
        mid = (low+high)//2
        res = min(res,arr[mid])
        if arr[mid] >= arr[low]:
            low = mid+1
        else:
            high = mid-1
    return res

arr1 = [2,3,4,5,6,7,8,9,10,1]
result1 = minInRotatedSorted(arr1,0,9)
#print(result1)


def subArraySum(arr,s):
    left = 0
    right = 0
    currentSum = 0
    while left < len(arr) and right < len(arr):
        if currentSum == s:
            return [left+1,right]
        elif currentSum < s:
            currentSum += arr[right]
            right += 1
        else:
            currentSum -= arr[left]
            left += 1
    return [-1]

arr2 = [1,2,3,4,5,6,7,8,9,10]
result2 = subArraySum(arr2,15)
#print(result2)


def countTwoRepeated(arr):
    result = []
    for i in range(len(arr)):
        index = abs(arr[i])
        if arr[index] > 0:
            arr[index] *= -1
        else:
            result.append(abs(arr[i]))
    return result

arr3 = [1,2,1,3,4,3]
result3 = countTwoRepeated(arr3)
print(result3)
