# 문제 이해 : https://www.acmicpc.net/board/view/54542
# 문제 해결 방법 : https://www.acmicpc.net/board/view/35331

N = int(input())

room = [input() for _ in range(N)]

row_count = 0
for line in room:
    dot = 0
    
    for i in line:
        if i == 'X':
            if dot > 1:
                row_count += 1
            dot = 0
        else:
            dot += 1

    if dot > 1:
        row_count += 1

col_count = 0
for i in range(N):
    temp = ""
    dot = 0

    for j in range(N):
        temp += (room[j][i])
    
    for j in temp:
        if j == 'X':
            if dot > 1:
                col_count += 1
            dot = 0
        else:
            dot += 1

    if dot > 1:
        col_count += 1

print(row_count, col_count)