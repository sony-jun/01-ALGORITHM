import sys
sys.stdin = open('영수증_input.txt')

# 총 금액
x = int(input())

# 물건의 종류의 수
n = int(input())

# 물건 가격과 개수
sum_ = 0
for i in range(n):
    price, count = map(int, input().split())
    
    sum_ += (price * count)
    
if x == sum_:
    print('Yes')
else:
    print('No')