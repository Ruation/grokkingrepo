def find_smallest(arr):
    smalest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smalest:
            smalest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    ArrSort = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        ArrSort.append(arr.pop(smallest))
    return ArrSort

print(selectionSort([1, 4, 5, 7, 9, 2 , 3, 8]))