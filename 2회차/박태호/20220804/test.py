import sys
sys.stdin = open('박스.txt','r')
n=4
m=5
grid = [
    ['1', '0', '1', '0', '1'],
    ['0', '0', '0', '1', '0'],
    ['0', '1', '0', '0', '1'],
    ['0', '0', '1', '0', '0']]


movecnt = 0
for i in range(n): # 4
    boxnum = (grid[i].count('1'))
    floor = m - 1
    for j in range(m-1,-1,-1):
        print(j)
        if grid[i][j] == '1':
            movecnt += floor - j
            floor -= 1
