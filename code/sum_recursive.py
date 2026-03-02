def sum_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        total = arr.pop(0) + sum_recursive(arr)
        return total
    
print(sum_recursive([1, 2, 3, 4, 5, 6]))