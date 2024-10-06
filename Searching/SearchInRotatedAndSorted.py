def searchInSortedAndRotatedArray(arr,ele):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        elif arr[low] <= arr[mid]:
            #Left Half Sorted Array
            if ele >= arr[low] and ele < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right Half Sorted array
            if ele > arr[mid] and ele <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
    

arr = [10,20,40,50,5,8]
result = searchInSortedAndRotatedArray(arr,6)
print(result)

def binarySearch(arr,low,high,ele):
    while low < high:
        mid = (low+high)//2

        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            high = mid-1
        else:
            low = mid+1
    return -1
