n = int(input())

result = [['.'] * n for _ in range(n)]
win = True

bomb = [['.'] * (n + 2)]
for _ in range(n):
    s = ['.'] + list(input()) + ['.']
    bomb.append(s)
bomb += [['.'] * (n + 2)]

check = [['.'] * (n + 2)]
for _ in range(n):
    c = ['.'] + list(input()) + ['.']
    check.append(c)
check += [['.'] * (n + 2)]

for i in range(1, n+1):
    for j in range(1, n+1):
        a = ""
        if check[i][j] == 'x':
            if bomb[i][j] == '*':
                win = False
                a = '*'
                result[i-1][j-1] = a
            else:
                a += bomb[i-1][j-1] + bomb[i-1][j] + bomb[i-1][j+1]+bomb[i][j-1] + \
                    bomb[i][j+1]+bomb[i+1][j-1] + bomb[i+1][j] + bomb[i+1][j+1]
                result[i-1][j-1] = str(a.count('*'))

if win == False:
    for i in range(1, n+1):
        for j in range(1, n+1):
            if bomb[i][j] == '*':
                result[i-1][j-1] = '*'

    for i in range(n):
        print(''.join(result[i]))
else:
    for i in range(n):
        print(''.join(result[i]))
