n = int(input())
mine = []
click = []
for _ in range(n):
    line = list(input())
    mine.append(list)

for _ in range(n):
    line = list(input())
    click.append(line)

open = []
for i in range(n):
    for j in range(n):
        if click[i][j] == 'X':
            if mine[i][j] =='*':
                print('*', end ='')
            else:
                around = []
                if i == 0 or j == 0:
                    