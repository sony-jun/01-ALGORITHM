n = 8
m = 8
result = []
knight = 0
for _ in range(n):
    line = list(input())
    result.append(line)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if result[i][j] == 'F':
                knight = knight + 1
print(knight)