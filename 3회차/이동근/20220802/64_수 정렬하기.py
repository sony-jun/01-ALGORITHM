import sys

input = sys.stdin.readline

N = int(input().strip())

l = []
for i in range(N):
    l.append(int(input().strip()))

l.sort()

for i in l:
    print(i)