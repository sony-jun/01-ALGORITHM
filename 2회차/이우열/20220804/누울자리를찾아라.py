n = int(input())

room = [list(input()) for _ in range(n)]
r_lie = []
c_lie = []

for i in range(n):
    r_can = 0
    c_can = 0

    for j in range(n):
        if room[i][j] != 'X':
            r_can += 1
        elif room[i][j] == 'X':
            r_lie.append(r_can)
            r_can = 0

        if room[j][i] != 'X':
            c_can += 1
        elif room[j][i] == 'X':
            c_lie.append(c_can)
            c_can = 0

    r_lie.append(r_can)
    c_lie.append(c_can)

r_cnt = 0
c_cnt = 0

for i in r_lie:
    if i >= 2:
        r_cnt += 1

for i in c_lie:
    if i >= 2:
        c_cnt += 1

print(r_cnt, c_cnt)
