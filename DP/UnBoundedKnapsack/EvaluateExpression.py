table = dict()
def evaluateExpression(s,i,j,isTrue):
    if i > j:
        return 0
    if i == j:
        if isTrue == True:
            return 1 if s[i] == 'T' else 0
        else:
            return 1 if s[i] == 'F' else 0
    temp = '{} {} {}'.format(i,j,isTrue)
    if temp in table:
        return table[temp]
    ans = 0
    for k in range(i+1,j,2):
        lt = evaluateExpression(s,i,k-1,True)
        lf = evaluateExpression(s,i,k-1,False)
        rt = evaluateExpression(s,k+1,j,True)
        rf = evaluateExpression(s,k+1,j,False)
        if s[k] == '&':
            if isTrue:
                ans += (lt*rt)
            else:
                ans += (lt*rf) + (lf*rt) + (lf*rf)
        elif s[k] == '|':
            if isTrue:
                ans += (lt*rf) + (lf*rt) + (lt*rt)
            else:
                ans += (lf*rf)
        elif s[k] == '^':
            if isTrue:
                ans += (lf*rt) + (lt*rf)
            else:
                ans += (lt*rt) + (lf*rf)
    table[temp] = ans
    return ans
            

input = 'T^F&T'
result = evaluateExpression(input,0,len(input)-1,True)
print(result)
