# 쉽게 푸는 문제
# 문제 : 수열(12233344445...)을 만들고 해당 구간에 속하는 숫자의 합 구하기
# 접근 : d

a, b = map(int, input().split())

data = [0]
sum = 0
# 수열 만들기
for i in range(1, b + 1):
    for j in range(i):
        data.append(i)

for i in range(a, b + 1):
    sum += data[i]

print(sum)
