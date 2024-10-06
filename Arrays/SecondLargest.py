def secondLargestElement(arr):
    result = -1
    largest = 0
    for i in range(len(arr)):
        if arr[i] > arr[largest]:
            result = largest
            largest = i
        elif arr[i] != arr[largest]:
            if result == -1 or arr[i] > arr[result]:
                result = i
    return result
    

arr = [10,78,34,78,65,43,89,65]
res = secondLargestElement(arr)
print(res)
