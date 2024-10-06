import math

def isPrime(num):
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    for i in range(5,int((math.sqrt(num))+1), 6):
        if num%i == 0 or num%(i+2) == 0:
            return False
    return True



"""
Time Complexity will be O(nlogn)
"""
def primeFactors(num):
    for i in range(2, num+1):
        if isPrime(i):
            x = i
            while(num%x ==0):
                print(i)
                x = x*i

def primeFactorEfficient(num):
    if num <= 1:
        return
    for i in range(2,(int(math.sqrt(num))+1)):
        while(num%i == 0):
            print(i)
            num = num//i
    if num > 1:
        print(num)


"""Time Complexity: The worst case happens when n is prime, it will execute every ietraion in
    for loop since while loop won't be executed. So it will be O(sqrt(n))

"""
def primeFactorMoreEfficient(num):
    if num <= 1:
        return
    while num%2 == 0:
        print(2)
        num = num//2
    while num%3 == 0:
        print(3)
        num = num//3
    for i in range(5, (int(math.sqrt(num)))+1, 6):
        while num%i == 0:
            print(i)
            num = num//i
        while (num+2)%i == 0:
            print(i+2)
            num = num//(i+2)
    if num > 3:
        print(num)
        

#primeFactors(12)
#primeFactorEfficient(23)
primeFactorMoreEfficient(450)
        
