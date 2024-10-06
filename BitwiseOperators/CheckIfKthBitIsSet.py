"""
Time Complexity; Θ(k)
"""
def isSet(num,k):
    x = 1
    for i in range(0,k-1):
        x = x*2
    if num&x != 0:
        print("kth bit is set")
        return True
    else:
        print("kth bit is not set")
        return False


def isSetAnother(num,k):
    for i in range(0,k-1):
        num = int(abs(num/2))
    if num & 1 != 0:
        print("kth bit is set")
        return True
    else:
        print("kth bit is not set")
        return False



def isSetEfficient(num,k):
    x = (1<<k-1)
    if num&x != 0:
        print("kth bit is set")
        return True
    else:
        print("kth bit is not set")
        return False

def isSetEfficientAnother(num,k):
    num = (num>>k-1)
    if num&1 != 0:
        print("kth bit is set")
        return True
    else:
        print("kth bit is not set")

result = isSetEfficient(10,3)
