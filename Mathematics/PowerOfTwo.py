"""
Time Complexity = Θ(logn)
"""
def isPowerOfTwo(num):
    if num == 0:
        return False
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            return False
    return True

def isPowerOfTwoEfficient(num):
    if num == 0:
        return False
    return num&(num-1) == 0

result = isPowerOfTwoEfficient(4)
print(result)
