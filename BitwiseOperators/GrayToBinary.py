def grayToBinary(n):
    return n ^ (n<<1)
    

#def grayToBinaryToDecimal(n):

result = grayToBinary(100)
print(result)
