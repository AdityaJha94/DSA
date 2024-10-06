def trailingZeroes(number):
    count = 0
    temp = number
    i = 5
    while i <= number:
        count = count + (number//i)
        i = i*5
    print(count)
    return count

number = 5
trailingZeroes(number)


"""
Time Complexity is Θ(logn) and it fixes the overflow problem
"""
