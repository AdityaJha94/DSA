def calculateGCD(first,second):
    temp = min(first,second)
    while temp > 0:
        if first%temp == 0 and second%temp == 0:
            break
        temp -= 1
    print(temp)
    return temp

calculateGCD(4,6)

"""
Time Complexity: O(min(a,b))
"""
