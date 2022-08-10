n = int(input())
cow = {}
cnt = 0
for i in range(n):
    number,position = map(int,input().split())
    if number not in cow:
        cow[number]=position
    else:
        if cow[number] != position:
            cow[number]=position    
            cnt+=1
print(cnt)