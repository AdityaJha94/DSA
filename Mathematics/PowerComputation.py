def powerComputation(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x

    result = 1
    for i in range(n):
        result = result*x
    return result


"""
Time Complexity: Θ(logn)
Auxiliary Space: Θ(logn)
"""

def powerOfComputationEfficient(x,n):
    if n == 0:
        return 1
    temp = powerOfComputationEfficient(x,n//2)
    temp = temp*temp
    if n%2 == 0:
        return temp
    else:
        return temp*x
        
    """
    if n == 1:
        return x
    result = 1
    if n%2 == 0:
        for i in range(n//2):
            result = result*x
        result = result*result
    else:
        result = powerOfComputationEfficient(x,n-1)*x
    
    return result
    """

def allDivisors(num):
    for i in range(1,num+1):
        if num%i == 0:
            print(i)

allDivisors(101)
"""
result = powerOfComputationEfficient(3,4)
print(result)
print(pow(3,4))
"""
