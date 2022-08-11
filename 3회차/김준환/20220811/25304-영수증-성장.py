total = int(input())
n = int(input())
s = 0
for _ in range(n):
    price, ct = map(int,input().split())
    s += price*ct
if s == total:
    print('Yes')
else:
    print('No')