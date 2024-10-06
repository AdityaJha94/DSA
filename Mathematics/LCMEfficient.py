def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a,b):
    lcm = (a*b)//gcd(a,b)
    return lcm

result = lcm(4,6)
print(result)


"""
Time Complexity:O(log(min(a,b)))
"""
