n = int(input())
cups = '123'
cnt=0
for i in range(n):
    x,y = input().split()
    if x == y:
        cups = cups
        cnt +=1
    else:
        cups = cups.replace(y,' ')
        cups = cups.replace(x,y)
        cups = cups.replace(' ',x)

if cnt==n:
    print(-1)
else:
    print(cups[0])