
def countDigits(number):
    count = 0
    while number > 0:
        number = number//10
        count += 1
    print(count)
    return count

countDigits(8967)

"""
Time Complexity: If d is the num,ber of digits then it is going to take Θ(d) time overall.
"""
