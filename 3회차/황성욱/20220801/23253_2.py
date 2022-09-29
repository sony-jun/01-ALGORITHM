import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 교과서의 수, 더미의 수

ans = []
for i in range(m):
    k = int(input())
    dum = list(map(int, input().split()))
    ans.append(dum)


for i in range(1, n + 1):
    for j in ans:
        if len(j) > 0 and j[-1] == i:
            j.pop()
            n -= 1

if n == 0:
    print('Yes')
else:
    print('No')