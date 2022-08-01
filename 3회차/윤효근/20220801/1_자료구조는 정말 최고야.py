import sys

sys.stdin = open("1_자료구조는 정말 최고야.txt")
n,m = map(int, input().split())
r = True
for _ in range(m):
    i = int(input())
    k = list(map(int, input().split()))
    for j in range(i - 1):
        if k[j] < k[j + 1]:
            r = False
            break
    if not r: break

print('Yes' if r else 'No')