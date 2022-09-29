# 2231
"""
"""
N = int(input())

# 분해합 후보를 순회
for number in range(1, N + 1):
    num = str(number)
    # 자릿 수의 합
    sum_ = sum(map(int, num))
    # 분해합
    hap = number + sum_
    
    if hap == N:
        print(number)
        break
else:
    print(0)
