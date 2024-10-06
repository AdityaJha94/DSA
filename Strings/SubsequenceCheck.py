def subsequenceCheck(str1, str2):
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            i += 1
    return j == len(str2)


str1 = 'ABCD'
str2 = 'AD'

result = subsequenceCheck(str1,str2)
print(result)
