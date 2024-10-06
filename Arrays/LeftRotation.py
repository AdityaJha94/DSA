"""
Time Complexity: Θ(n*d)
Space Complexity: Θ(1)
"""
def leftRotate(arr,d):
    temp = arr[0]
    for i in range(d):
        leftRotateByOne(arr)
    print(arr)

def leftRotateByOne(arr):
    temp = arr[0]
    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1]
    arr[len(arr)-1] = temp

arr = [1,2,3,4,5]
#leftRotate(arr,2)


"""
Time Complexity: Θ(n+d)
Space Complexity: Θ(d)
"""

def leftRotateEfficient(arr,d):
    if d%(len(arr)) != 0:
        d = d%len(arr)
    else:
        d = len(arr)

    temp = [0]*d
    for i in range(d):
        temp[i] = arr[i]
    for i in range(d,len(arr)):
        arr[i-d] = arr[i]
    for i in range(d):
        arr[len(arr)-d+i] = temp[i]
    print(arr)
#leftRotateEfficient(arr,39)

"""
Time Complexity: Θ(n)
Space Complexity: Θ(1)
"""

def leftRotateMoreEfficient(arr,d):
    if d%(len(arr)) != 0:
        d = d%len(arr)
    else:
        d = len(arr)
    reverse(arr,0,d-1)
    reverse(arr,d,len(arr)-1)
    reverse(arr,0,len(arr)-1)
    print("test")
    print(arr)


def reverse(arr,low, high):
    while low < high:
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high -= 1

leftRotateMoreEfficient(arr,60)
