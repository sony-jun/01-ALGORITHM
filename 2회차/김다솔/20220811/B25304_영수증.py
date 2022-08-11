# https://www.acmicpc.net/problem/25304
import sys
sys.stdin = open('B25304.txt')
X = int(input())
N = int(input())
compare = []
for _ in range(N):
    a, b = map(int, input().split())
    compare.append(a*b)
if sum(compare) == X:
    print('Yes')
else:
    print('No')    