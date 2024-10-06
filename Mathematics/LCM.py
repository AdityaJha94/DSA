def lcm(a,b):
    temp = max(a,b)
    while True:
        if temp%a == 0 and temp%b == 0:
            return temp
        temp += 1
    return temp


result = lcm(7,3)
print(result)
            
    
"""
Upper bound on time complexity is O(a*b) and to be more precsie it will be
O(a*b - max(a,b))

"""
