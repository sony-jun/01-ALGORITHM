'''
문제>
오목 : 5개의 돌이 연속으로 놓여져있으면 이기는 게임.

6개일 경우 육목이므로 (오목이 아니므로) 무효.

검은색 1
흰돌 2

어느돌이 이겼는지 출력


'''

baduk = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

valid = False
for i in range(19):
    for j in range(19):
        target = baduk[i][j]
        if baduk[i][j] != 0:
            for d in range(4):
                cnt = 1
                r = i + dx[d]
                c = j + dy[d]

                while 0 <= r < 19 and 0 <= c < 19 and baduk[r][c] == target:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= i - dx[d] < 19 and 0 <= j - dy[d] < 19 and baduk[i-dx[d]][j-dy[d]] == target:
                            break
                        if 0 <= r + dx[d] < 19 and 0 <= c + dy[d] < 19 and baduk[r+dx[d]][c+dy[d]] == target:
                            break
                        valid = True
                        print(target)
                        print(i + 1, j + 1)
                           
                    r += dx[d]
                    c += dy[d]
if not valid:
    print(0)
             
             