def plusOneReverseLoopApproach(arr):
    digits = arr
    i = len(arr)-1
    while i > 0:
        if arr[i] == 9:
            digits[i] = 0
            i -= 1
        else:
            digits[i] = arr[i]+1
            break
        
    if i == 0:
        if arr[i] == 9:
            digits[i] = 0
            digits.insert(0,1)
        else:
            digits[i] == arr[i]+1
    print(digits)

    
def plusOneForwardLoopApproach(arr):
    digits = arr[::-1]
    i = 0
    one = 1
    while one:
        if i < len(arr):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i]+1
                one = 0
        else:
            digits.append(1)
            one = 0
        i += 1
    print(digits[::-1])

arr = [9,9,9]
result = plusOneForwardLoopApproach(arr)
