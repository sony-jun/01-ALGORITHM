import sys
input = sys.stdin.readline
N = int(input())
customers = list(map(int, input().split()))
table = [0] * 101
cnt = 0
for customer in customers:
    if table[customer] != 0:
        cnt += 1
    else:
        table[customer] = 1
print(cnt)
