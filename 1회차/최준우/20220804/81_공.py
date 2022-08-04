# https://www.acmicpc.net/problem/1547

M = int(input())
cups = [1, 0, 0]
temp = 0

for i in range(M):
    x, y = map(int, input().split())
    
    temp = cups[x-1]
    cups[x-1] = cups[y-1]
    cups[y-1] = temp

for i in range(len(cups)):
    if cups[i] == 1:
        print(i+1)
        break
else:
    print(-1)