n = int(input())
arr = [ x for x in range(1, n + 1)]

while n > 1:
    print(arr[0], end=' ')
    arr.pop(0)
    arr.append(arr[0])
    arr.pop(0)
    
    n -= 1
print(arr[0])
