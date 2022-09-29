import sys
input = sys.stdin.readline
n=int(input())
m=[int(input()) for i in range(n)]
m=sorted(m)
for _ in range(n):
    print(m.pop(0))
