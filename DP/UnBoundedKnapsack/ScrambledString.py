table = dict()
def isScrambleString(s1,s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    if len(s1) <= 1:
        return False
    n = len(s1)
    temp = "{} {}".format(s1,s2)
    if temp in table:
        return table[temp]
    for i in range(1,n):
        print(i)
        print("Compare this two")
        print(s1[0:i])
        print(s2[(n-i):n])
        print("Compare this two")
        print(s1[i:n])
        print(s2[0:(n-i)])
        print("Compare this two")
        print(s1[0:i])
        print(s2[0:i])
        print("Compare this two")
        print(s1[i:n])
        print(s2[i:n])
        print('**********************************')
        cond1 = isScrambleString(s1[0:i], s2[(n-i):n]) and isScrambleString(s1[i:n],s2[0:(n-i)])
        cond2 = isScrambleString(s1[0:i], s2[0:i]) and isScrambleString(s1[i:n],s2[i:n])
        if cond1 or cond2:
            table[temp] = True
            return True
    table[temp] = False
    return False
                                            

s1 = 'abcde'
s2 = 'caebd'
result = isScrambleString(s1,s2)
print(result)
