num = 0 # 순서
sum_ = 0 # 최대값
for i in range(5):
    a, b, c, d = map(int, input().split())
    result = a + b + c + d

    if sum_ < result: #최대값 비교
        num = i + 1 # 최대값 순서
        sum_ = result
print(num, sum_) 