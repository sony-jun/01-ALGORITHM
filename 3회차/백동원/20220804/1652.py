# 누울 자리를 찾아라

N = int(input())
room = [list(input()) for _ in range(N)]
a_cnt = 0
b_cnt = 0
for a in range(N):
    cnt = 0
    for b in range(N):
        if room[a][b] == '.':
            cnt += 1
        elif room[a][b] == 'X':
            if cnt >= 2 :
                a_cnt += 1
                cnt = 0
            else:
                cnt = 0
    if cnt >= 2:
        a_cnt += 1

for a in range(N):
    cnt = 0
    for b in range(N):
        if room[b][a] == '.':
            cnt += 1
        elif room[b][a] == 'X':
            if cnt >= 2 :
                b_cnt += 1
                cnt = 0
            else:
                cnt = 0
    if cnt >= 2:
        b_cnt += 1

print(a_cnt, b_cnt)