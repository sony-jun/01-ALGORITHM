import sys
sys.stdin = open('test.txt', 'r')

y, x = list(map(int, input().split()))
pic = []
check = []
for _ in range(y):
    line = list(map(int, input().split()))
    hang = []
    for _ in range(x):
        hang.append(0)
    pic.append(line)
    check.append(hang)
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j):
    stack = [[i, j]]
    check[i][j] = 1
    cnt = check[i][j]

    while stack:
        cur = stack.pop()
        for c in range(4):
            ni = di[c] + cur[0]
            nj = dj[c] + cur[1]
            if ni in range(y) and nj in range(x):
                if pic[ni][nj] == 1:
                    pic[ni][nj] = 0
                    cnt += 1
                    check[ni][nj] = cnt
                    stack.append([ni, nj])
    return cnt

pic_cnt = 0
largest = 0
for i in range(y):
    for j in range(x):
        if pic[i][j] == 1:
            pic[i][j] = 0
            pic_cnt += 1
            length = dfs(i, j)
            if length > largest:
                largest = length
if pic_cnt == 0:
    print(0)
    print(0)
else:
    print(pic_cnt)
    print(largest)