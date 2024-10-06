
def isSafe(arr,i,j):
    return i < len(arr) and j < len(arr) and arr[i][j] == 1


def ratInAMaze(arr,sol,i=0,j=0):
    if i == len(arr)-1 and j == len(arr)-1 and arr[i][j] == 1:
        print("i: ", i , "j: ", j)
        sol[i][j] = 1
        print("sol after assigning: ", sol)
        return True
    if isSafe(arr,i,j) == True:
        print("i: ", i , "j: ", j)
        sol[i][j] = 1
        print("sol after assigning: ", sol)
        if ratInAMaze(arr,sol,i+1,j) == True:
            return True
        if ratInAMaze(arr,sol,i,j+1) == True:
            return True
        print("Blocked:-  ", "i: ", i , "j: ", j)
        sol[i][j] = 0
            
    return False

def solveMaze(arr):
    sol = [[0]*len(arr) for i in range(len(arr))]
    if ratInAMaze(arr,sol,0,0) == False:
        return False
    print(sol)
    return True
        
    

arr = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
result = solveMaze(arr)
print(result)
