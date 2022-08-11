total_amount = int(input()) # 영수증에 적힌 총 금액
times = int(input()) # 영수증에 적힌 구매한 물건의 종류의 수

for i in range(times):
    a, b = input().split() # a = 각 물건의 가격, b = 개수
    a, b = int(a), int(b)

    total_amount -= (a*b)

print("Yes" if total_amount == 0 else "No") # 영수증의 총 금액과 일치하면 Yes


