m,n = map(int,input().split())
x,y = 0,0
direction = [(1,0),(0,1),(-1,0),(0,-1)]
answer = "well"
for i in range(n):
    order,num = input().split()
    if order == 'TURN':
        if num == '0':
            direction.append(direction.pop(0))
        else:
            direction.insert(0,direction.pop())
    else:
        x = x+(int(num)*direction[0][0])
        y = y+(int(num)*direction[0][1])
    if not (0<=x<m+1 and 0<=y<m+1):
        answer = 'error'
if answer == 'error':
    print(-1)
else:
    print(x,y)
    


