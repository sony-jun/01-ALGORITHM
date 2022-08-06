def cnt(i, j, seet, n):
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    mine = 0
    for _ in range(8):
        ni = i + di[_]
        nj = j + dj[_]
        if 0 <= ni < n and 0 <= nj < n:
            if seet[ni][nj] == '*':
                mine += 1
    return mine

n = int(input())
m_seet = []
c_seet = []

for _ in range(n):
    sen = list(input())
    m_seet.append(sen)

for _ in range(n):
    sen = list(input())
    c_seet.append(sen)

mine_touch = 0
open_seet = []
for i in range(n):
    line = []
    for j in range(n):
        if c_seet[i][j] == 'x':
            line.append(cnt(i, j, m_seet, n))
            if m_seet[i][j] == '*':
                mine_touch = 1
        else:
            line.append('.')
    open_seet.append(line)

if mine_touch == 1:
    for i in range(n):
        for j in range(n):
            if m_seet[i][j] == '*':
                open_seet[i][j] = '*'

for i in range(len(open_seet)):
    for  j in open_seet[i]:
        print(j, end = '')
    print()

