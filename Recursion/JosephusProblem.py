"""
Time Complexity: θ(n)
"""

def josephusSurvivor(n,k):
    if n == 1:
        return 0
    return (josephusSurvivor(n-1,k) + k)%n

result = josephusSurvivor(8,2)
print(result)
