import sys




n,m = map(int,input().split())

y=n
x=0 

turn = [(0,1),(1,0),(0,-1),(-1,0)]

ran =0
tc = 0
for __ in range(m):
    command,c = sys.stdin.readline().rstrip().split()
    if command == 'TURN':
        if c == '1':
            tc+=1
            if tc == 4 :
                tc=0
        elif c == '0':
            tc-=1
            if tc == -1:
                tc=3
    elif command == 'MOVE':
        move = turn[tc]
        ny= y+(move[0]*int(c))
        nx= x+(move[1]*int(c))
        if 0>ny or ny>n or 0>nx or nx >n:
            ran=1
        else:
            y=ny
            x=nx

if ran==1:
    print(-1)
else:
    print(x,n-y)
