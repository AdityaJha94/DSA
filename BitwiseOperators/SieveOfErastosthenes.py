import math

#Sieve of Eratosthenes
def SOE(num):
    tempArr = [True]*(num+1)
    print(tempArr)
    for i in range(2,(int(math.sqrt(num)))+1):
        if tempArr[i] == True:
            for j in range(i*i,num+1,i):
                tempArr[j] = False

    for i in range(2,num+1):
        if tempArr[i] == True:
            print(i)

"""
Time Complexity: O(loglogn)
"""
def SOEEfficient(num):
    tempArr = [True]*(num+1)
    for i in range(2,num+1):
        if tempArr[i] == True:
            print(i)
        for j in range(i*i,num+1,i):
            tempArr[j] = False

result = SOEEfficient(23)
