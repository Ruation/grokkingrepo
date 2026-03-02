def maxnum(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
print (maxnum([1, 2, 4, 2, 1, 3, 10]))