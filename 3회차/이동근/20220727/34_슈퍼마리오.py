l = []
for _ in range(10):
    l.append(int(input()))

result = 0
pre = 0
i = 0

for i in range(10):
    if result <= 100:
        result += l[i]
        pre = l[i]

# 100 에 가까운 값이 2개가 있을 경우 큰 녀석을 선택하므로 부등호는 < 이 아닌 <= 이다.
result = result if abs(100 - result) <= abs(100 - (result - pre)) else result - pre

print(result)