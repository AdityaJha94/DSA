import math

def isSafe(i,j,x,n,board):
    for k in range(n):
        if board[k][j] == x or board[i][k] == x:
            return False
    s = int(math.sqrt(n))
    rs = i - i%s
    cs = j - j%s
    for l in range(s):
        for m in range(s):
            if board[l+rs][m+cs] == x:
                return False
    return True
    
    
def solve(n,board):
    i = 0
    j = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                break
    if i == n and j == n:
        return True
    for x in range(1,n+1):
        if isSafe(i,j,x,n,board):
            board[i][j] = x
            if solve(n,board) == True:
                return True
            board[i][j] = 0
    return False
            
def sudokuSolver(n,board):
    if solve(n,board) == True:
        print(board)
    else:
        print("Not Possible")

board = [[3,0,6,5,0,8,4,0,0],
[5,2,0,0,0,0,0,0,0],
[0,8,7,0,0,0,0,3,1],
[0,0,3,0,1,0,0,8,0],
[9,0,0,8,6,3,0,0,5],
[0,5,0,0,9,0,6,0,0],
[1,3,0,0,0,0,2,5,0],
[0,0,0,0,0,0,0,7,4],
[0,0,5,2,0,6,3,0,0]]
sudokuSolver(9,board)
