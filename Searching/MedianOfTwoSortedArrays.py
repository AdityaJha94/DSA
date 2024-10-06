def calculateMedian(arr1,arr2,n,m):
    low = 0
    high = n
    while low <= high:
        i1 = (low+high)//2
        i2 = ((n+m+1)//2) - i1
        min1 = float('inf') if i1 == n else arr1[i1]
        max1 = float('-inf') if i1 == 0 else arr1[i1-1]
        min2 = float('inf') if i2 == m else arr2[i2]
        max2 = float('-inf') if i2 == 0 else arr2[i2-1]
        if max1 <= min2 and max2 <= min1:
            if (n+m)%2 == 0:
                return float((max(max1,max2) + min(min1,min2))/2)
            else:
                return float(max(max1,max2))
        elif max1 > min2:
            high = i1-1
        else:
            low = i1+1

                

def medianOfTwoSortedArrays(arr1,arr2,n,m):
    if n > m:
        return calculateMedian(arr2,arr1,m,n)
    else:
        return calculateMedian(arr1,arr2,n,m)

arr1 = [10,12,14,16,18,20]
arr2 = [2,3,5,8]
result = medianOfTwoSortedArrays(arr1,arr2,6,4)
print(result)

    
