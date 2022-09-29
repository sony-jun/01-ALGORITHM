bill = int(input())
kind = int(input())
sum = 0
for _ in range(kind):
    price, cnt = list(map(int, input().split()))
    sum += price * cnt
if bill == sum:
    print('Yes')
else:
    print('No')