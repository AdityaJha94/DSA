def anagramCheck(str1,str2):
    if len(str1) != len(str2):
        return False
    count = [0]*256
    for i in range(len(str1)):
        count[ord(str1[i]) - ord('a')] += 1
        count[ord(str2[i]) - ord('a')] -= 1
    for i in range(len(count)):
        if count[i] != 0:
            return False
    return True

str1 = 'aabca'
str2 = 'acaba'
result = anagramCheck(str1,str2)
print(result)
              
              


              
