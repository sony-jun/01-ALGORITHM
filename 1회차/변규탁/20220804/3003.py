chess = [1, 1, 2, 2, 2, 8]

white = list(map(int, input().split()))

answer = []
for i in range(len(chess)):
    if chess[i] < white[i]:
        answer.append(chess[i] - white[i])
    elif chess[i] > white[i]:
        answer.append(chess[i] - white[i])
    else:
        answer.append(0)

print(*answer)
