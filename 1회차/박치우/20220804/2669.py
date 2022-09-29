empty_square = [[0] * 100 for _ in range(100)]
count = 0

for i in range(4):
    x1 , y1 , x2, y2 = map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            empty_square[j][k] += 1

for i in range(100):
    for j in range(100):
        if empty_square[i][j] != 0:
            count += 1
print(count)

