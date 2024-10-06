"""
Time Complexity: O(n*n)
Space Complexity: Θ(1)
"""
def leadersInArray(arr):
    for i in range(0,len(arr)):
        flag = False
        for j in range(i+1,len(arr)):
            if arr[j] >= arr[i]:
                flag = True
                break
        if not flag:
            print(arr[i])

arr = [7,10,4,3,6,5,2]
#leadersInArray(arr)

"""
Time Complexity: Θ(n)
Space Complexity: Θ(1)
"""             
def leadersInArrayEfficient(arr):
    i = len(arr)-2
    currentMax = arr[len(arr)-1]
    print(arr[len(arr)-1])
        
    while i >= 0:
        if arr[i] > currentMax:
            print(arr[i])
            currentMax = arr[i]
        i -= 1

leadersInArrayEfficient(arr)
