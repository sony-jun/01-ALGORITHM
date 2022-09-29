N = int(input())
seat = list(map(int,input().split()))
li = []
cnt = 0

for i in seat:
    if i in li:
        cnt += 1
    else:
        li.append(i)

print(cnt)