chess = [1, 1, 2, 2, 2, 8]
input_chess = list(map(int, input().split()))
result = []
for i in range(len(chess)):
    insert = chess[i] - input_chess[i]
    result.append(insert)
print(*result)