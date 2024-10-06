"""
Time Complexity: O(3^n)
"""
def maxPiecesRopeCutting(n,a,b,c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    result = max(maxPiecesRopeCutting(n-a,a,b,c),maxPiecesRopeCutting(n-b,a,b,c),
                 maxPiecesRopeCutting(n-c,a,b,c))
    if result == -1:
        return -1
    else:
        return result+1

result = maxPiecesRopeCutting(23,11,9,12)
print(result)





                 
    
