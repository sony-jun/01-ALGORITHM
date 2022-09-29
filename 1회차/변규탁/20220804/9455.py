T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    box_col = []
    for i in range(M):
        temp = []
        for j in range(N):
            temp.append(box[j][i])
        box_col.append(temp)

    answer = 0
    for col in box_col:
        for i in range(len(col)):
            if col[i] == 1:
                count_ = col[i+1:].count(0)
                answer += count_ 

    print(answer)