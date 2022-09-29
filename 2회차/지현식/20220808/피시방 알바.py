import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int ,input().split()))
check = []
cnt = 0
for i in lst:
    if i not in check:
        check.append(i)
    else:
        cnt += 1
print(cnt)