N, M = map(int, input().split())

parking = [list(input()) for _ in range(N)]

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

answer = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0
}
valid = True
for i in range(N-2+1):
    for j in range(M-2+1):
        cnt = 0
        for d in range(4):
            r = i + dx[d]
            c = j + dy[d]
            if parking[r][c] == '#':
                valid = False
                break
            elif parking[r][c] == 'X':
                cnt += 1
                valid = True
            valid = True
        if valid :
            answer[cnt] += 1

print(*answer.values(), sep='\n')