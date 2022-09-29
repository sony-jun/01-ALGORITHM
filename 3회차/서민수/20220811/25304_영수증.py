# 영수증에 적힌,

# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액
# 을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

# 입력
# 첫째 줄에는 영수증에 적힌 총 금액 $X$가 주어진다.

# 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 $N$이 주어진다.

# 이후 $N$개의 줄에는 각 물건의 가격 $a$와 개수 $b$가 공백을 사이에 두고 주어진다.

import sys


sys.stdin = open("input.txt")

# 총 금액
X = int(input())
# 물건 종류 수
N = int(input())

# 물건의 수와 가격을 곱을 담을 변수
sum_= 0
# 종류의 수
for _ in range(N):
    # 가격과 개수
    a,b = map(int,input().split())
    # 물건과 개수의 곱을 담아줌
    sum_ += a*b
# 총금액과 sum이 같다면
if X == sum:
    # yes
    print('Yes')
else:
    # no
    print("No")