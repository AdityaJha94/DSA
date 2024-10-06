def coinChangeRecursive(coins,n,s):
    if s == 0:
        return 1
    if s < 0:
        return 0
    if n == 0:
        return 0
    return coinChangeRecursive(coins,n,s-coins[n-1]) + coinChangeRecursive(coins,n-1,s)

coins = [2,5,3]
result = coinChangeRecursive(coins,3,5)
print(result)     
