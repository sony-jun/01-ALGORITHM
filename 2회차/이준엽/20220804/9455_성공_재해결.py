from dis import dis


t = int(input())
for i in range(t):
    m,n = map(int,input().split())
    grid = [list(map(int,input().split())) for i in range(m)]
    gblack = [0 for i in range(n)]
    dst = 0
    for i in range(n):
        for j in range(m):
            if grid[j][i] == 1:
                gblack[i]+=1
    for i in range(n):
        for j in range(m):
            if grid[j][i] == 1:
                dst+=(m-j-gblack[i])
                gblack[i]-=1
    print(dst)





t = int(input())
for i in range(t):
    box = 1
    emt = 0

    m,n = map(int,input().split())
    b_list = [list(map(int,input().split())) for i in range(m)]

    distance = 0

    for x in range(n):
        for y in reversed(range(m)):
            if b_list[y][x] == box:
                while True:
                    if y+1 == m:
                        break
                    if b_list[y+1][x] == box:
                        break
                    b_list[y][x] = emt
                    b_list[y+1][x] = box
                    y+=1
                    distance+=1
    print(distance)