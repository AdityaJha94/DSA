def stockBuyAndSell1(arr):
    profit = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit

arr = [30,20,10]
result = stockBuyAndSell1(arr)
print(result)
