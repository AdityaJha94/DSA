def moveZeroesToEnd(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[count] = arr[count],arr[i]
            count += 1
    print(arr)

arr = [0,10,0,0]
moveZeroesToEnd(arr)
