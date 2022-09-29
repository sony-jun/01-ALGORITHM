x = int(input())
n = int(input())
sum_price = 0
for i in range(n):
    a,b = map(int,input().split())
    sum_price+=a*b
if x == sum_price:
    print('Yes')
else:
    print('No')