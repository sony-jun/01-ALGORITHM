direc = [0,0,0,0] # 상 좌 하 우
i = 3
breaker = False
m, n = map(int,input().split())

for _ in range(n):
    order = list(input().split())
    if order[0] == 'MOVE':
        direc[i] += int(order[1])
        if direc[0] - direc[2] < 0 or direc[0] - direc[2] > m or direc[3] - direc[1] < 0 or direc[3] - direc[1] > m:
            breaker = True
    elif order[0] == 'TURN':
        if order[1] == '0':
            i += 1
        else :
            i -= 1
    i %= 4
            
if breaker == False:
    print(direc[3]-direc[1],direc[0]-direc[2])
else:
    print(-1)