def trailingZeroes(number):
    temp = factorial(number)
    count = 0
     
    while temp%10 == 0:
        count += 1
        temp = temp//10
    print(count)
    return count
        
def factorial(number):
    if number == 0 or number == 1:
        return 1
    result = 1
    for i in range(2,number+1):
        result = result*i
    print(result)
    return result
    
                   
number = 100
trailingZeroes(number)
                   
                   
                   
"""
Overall Time Complexity is Θ(n)
It is not an efficient solution as it will cause overflow issues for even smaller value of n.
The factorial of 20 will have 19 digits and our datatype won't be able to store it.
"""
