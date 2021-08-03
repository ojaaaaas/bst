#rearrange array succh that a[i] = i
def rearr(arr,n):
    arr1 = []
    for i in range(0,n-1):
        if arr[i] == i:
            arr1.append(i)
        else:
            arr1.append(-1)
    return arr1

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
n = len(arr)
print(rearr(arr,n))
