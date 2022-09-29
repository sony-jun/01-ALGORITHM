import sys
sys.stdin = open('25304.txt')

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
total = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    total += (a*b)

if total == X:
    print('Yes')
else:
    print('No')