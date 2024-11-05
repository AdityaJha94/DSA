def previousGreaterElement(arr: [int]) -> [int]:
    result = []
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] > stack[-1]:
            stack.pop()
        result.append(-1 if not stack else stack[-1])
        stack.append(arr[i])
    return result

arr = [15,10,18,12,4,6,2,8]
arr1 = [8,10,12]
result = previousGreaterElement(arr1)
print(result)
