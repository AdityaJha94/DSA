
"""
Time Complexity = Θ(d) where d is the number of bits from last to MSB
"""
def countNumberOfBits(num):
    count = 0
    while num > 0:
        if num%2 != 0:
            count += 1
        num = num//2
    return count

def countNumberOfBitsEfficient(num):
    count = 0
    while num > 0:
        count = count + (num&1)
        num = num >> 1
    return count

"""
Time Complexity = Θ(k) where k is the number of set bits from last to MSB
"""

def countNumberOfBitsMoreEfficient(num):
    count = 0
    while num > 0:
        num = num&(num-1)
        count += 1
    return count

"""
Time Complexity = Θ(1) where d is the number of bits from last to MSB
"""
def countNumberOfBitsLookUpTable(num):
    tbl = [0]*256
    for i in range(1,256):
        tbl[i] = tbl[i&(i-1)] + 1
    return tbl[num&255] + tbl[(num>>8)&255] + tbl[(num>>16)&255] + tbl[(num>>24)]
result = countNumberOfBitsLookUpTable(13)
print(result)
