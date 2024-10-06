def isPalindrome(number):
    flag = False
    temp = number
    reverseNum = 0
    while temp > 0:
        reverseNum = reverseNum*10 + (temp%10)
        temp = temp//10
    if number == reverseNum:
        print("palindrome")
        return True
    else:
        print("not palindrome")
        return False

isPalindrome(8668)

"""
Time Complexity: If d is the num,ber of digits then it is going to take Θ(d) time overall.
"""
