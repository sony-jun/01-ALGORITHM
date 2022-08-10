n,m = map(int,input().split())
nx,ny,mx,my = 0,0,0,0
if n%4 != 0:
    nx = n//4+1
    ny = n%4
else:
    nx = n//4
    ny = 4
if m%4 != 0:
    mx = m//4+1
    my = m%4
else:
    mx = m//4
    my = 4
result = abs(nx-mx)+abs(ny-my)
print(result)