import sys


sys.stdin = open('1236.txt')

n , m = map(int , input().split())
result = 0
castle = []
a= 0
b =0
for _ in range(n):
    line = list(input())
    castle.append(line)

for i in range(n):
    if 'X' not in castle[i]:
        a = a+ 1
for j in range(m):
    if "X" not in [castle[i][j] for i in range(n)]:
        b = b + 1
print(max(a,b))