import math


"""
Time COmplexity: O(sqrt(n))
"""
def allDivisors(num):
    k = 0
    for i in range(1, (int(math.sqrt(num)))+1):
        k = i
        if num % i == 0:
            print(i)
    #print(k)
    for j in range(k,0,-1):
        if num%j == 0:
            print(num//j)

allDivisors(90)
