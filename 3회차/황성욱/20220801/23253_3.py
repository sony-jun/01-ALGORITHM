
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 교과서의 수, 더미의 수

ans = []
is_sq = []
for i in range(m):
    k = int(input())
    dum = list(map(int, input().split()))
    if sorted(dum, reverse= True) != dum:
        is_sq.append('fail')

if len(is_sq) > 0:
    print('No')
else:
    print('Yes')

