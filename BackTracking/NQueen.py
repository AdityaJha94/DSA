def isSafe(result,row,column,n):
    for i in range(column):
        if result[row][i] == 1:
            return False
    i = row
    j = column
    while i >= 0 and j >= 0:
        if result[i][j] == 1:
            return False
        i -= 1
        j -= 1
    k = row
    l = column
    while k < n and l >= 0:
        if result[k][l] == 1:
            return False
        k += 1
        l -= 1
    return True
    
    
def solveNQueen(result, col,n):
    if col >= n:
        return True
    for i in range(n):
        if isSafe(result,i,col,n):
            result[i][col] = 1
            if solveNQueen(result,col+1,n) == True:
                return True
            result[i][col] = 0
    return False
    
def nQueen(n):
    result = [[0]*n for i in range(n)]
    if solveNQueen(result,0,n):
        print(result)
    else:
        print("Not Possible")

res = nQueen(4)


