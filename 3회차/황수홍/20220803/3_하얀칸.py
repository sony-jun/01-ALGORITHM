from sys import stdin

chess = []
for _ in range(8):
    chess.append(list(map(str, list(stdin.readline()))))

answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if chess[i][j] == 'F':
                answer += 1
print(answer)