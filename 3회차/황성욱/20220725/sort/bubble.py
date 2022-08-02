def bubble(arr):
    length = len(arr)-1
    for i in range(length):
        for j in range(length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

