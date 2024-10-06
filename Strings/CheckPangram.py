def checkPangram(s):
    count = [0]*26
    s = ''.join(letter for letter in s if letter.isalnum()).lower()
    for char in s:
        count[ord(char)-ord('a')] += 1
    for i in range(len(count)):
        if count[i] == 0:
            return False
    return True

s = 'Bawds jog, flick quartz, vex nymph'
result = checkPangram(s)
print(result)
                   
