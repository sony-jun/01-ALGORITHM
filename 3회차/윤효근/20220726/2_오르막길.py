import sys

sys.stdin = open("2_오르막길.txt")

a = int(input())
b =list(map(int,input().split()))
start = 0
result=[]
for i in range(a-1):
    if b[i] <b[i+1]:
        start += b[i+1] - b[i]
    else:
        result.append(start)
        start = 0
result.append(start)

print(max(result))