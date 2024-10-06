def reverseString(inputStr):
    start = 0
    for end in range(len(inputStr)):
        if inputStr[end] == ' ':
            performReverse(inputStr,start,end-1)
            print(start)
            print(end)
            print(inputStr)
            print("===========================================")
            start = end+1
    performReverse(inputStr,start,len(inputStr)-1)
    performReverse(inputStr,0,len(inputStr)-1)
    return inputStr

def performReverse(inputStr,i,j):
    print(f"inputSTR before:- ", inputStr)
    while i > j:
        inputStr[i],inputStr[j] = inputStr[j],inputStr[i]
        i += 1
        j -= 1
    print(f"inputSTR after:- ", inputStr)
    
inputStr = 'Welcome to GFG'
result = reverseString(inputStr)
print(result)
