"""
Time Complexity = O(n)
Space Complexity = O(n)
"""
def stockSpan(arr: [int]) -> [int]:
    stack = []
    result = []
    result.append(1)
    stack.append((arr[0],1))
    i = 1
    while i < len(arr):
        span = 1
        while stack and arr[i] >= stack[-1][0]:
            span += stack[-1][1]
            stack.pop()
        stack.append((arr[i],span))
        result.append(span)
        i += 1
    return result

arr = [13,15,12,14,16,8,6,4,10,30]
arr1 = [100,80,60,70,60,75,85]
result = stockSpan(arr1)
print(result)
        
    
