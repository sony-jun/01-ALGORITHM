arr = [
    [1,2,3,4],
    [5,6,7,8]]

for x in range(len(arr[0])):  # 열 개수
    for y in range(len(arr)): # 행 개수
        print(arr[y][x], end=' ')
    print()
