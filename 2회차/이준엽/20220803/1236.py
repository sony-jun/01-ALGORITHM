n, m = map(int,input().split())
matrix = [list(input()) for i in range(n)]
judge = ['']*m
lcnt = 0
for line in matrix:
    if 'X' not in line:
        lcnt +=1
    for _ in range(m):
        if line[_] == 'X':
            judge[_] = 'X'

if lcnt > judge.count(''):
    print(lcnt)
else:
    print(judge.count(''))