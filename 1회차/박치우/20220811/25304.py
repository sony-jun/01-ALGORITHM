money = int(input())
test_case = int(input())
total_price = 0

for i in range(test_case):
    price, count = map(int,input().split())
    total_price += price * count

if money == total_price:
    print('Yes')
else:
    print('No')