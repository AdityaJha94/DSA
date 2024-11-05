def nextGreaterElement(arr: [int]) -> [int]:
    result = [None]*len(arr)
    stack = []
    result[len(arr)-1] = -1
    stack.append(arr[-1])
    for i in range(len(arr)-2,-1,-1):
        while stack and arr[i] >= stack[-1]:
            stack.pop()
        result[i] = -1 if not stack else stack[-1]
        stack.append(arr[i])
    return result

arr = [5,15,10,8,6,12,9,18]
arr1 = [10,15,20,25]
result = nextGreaterElement(arr1)
print(result)
