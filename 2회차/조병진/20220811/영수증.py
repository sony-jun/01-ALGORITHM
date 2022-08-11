# 영수증 🐳
# 문제 : 구매한 물건의 가격과 영수증에 적힌 금액이 일치하는지 확인하기

X = int(input())
N = int(input())

items = [list(map(int, input().split())) for _ in range(N)]  # 이차원 리스트로 입력

total = 0
for i in items:  # 리스트를 하나씩 반복
    price = i[0] * i[1]
    total += price

if X == total:
    print('Yes')
else:
    print('No')
