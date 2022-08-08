n,m=map(int, input().split())
maze=[input() for _ in range(n)]

x=0
y=0
step=0
print(maze)
for _ in range(n*m):
    if maze[y][x+1] == 1:
        x+=1
        step+=1
    elif maze[y+1][x]== 1:
        y+=1
        step+=1
    else :
        try:
            if maze[y-1][x]== 1:
                y-=1
                step+=1
        except: 
            continue
    if x == n-1 and y == m-1 :
        break
print(step)