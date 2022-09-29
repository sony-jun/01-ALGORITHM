# 문제 : 자연수 n(분해합)의 가장 작은 생성자 구하기
# 입력 : 216
# 출력 : 198

# 분해합이란, N과 N의 각 자릿수의 합 💡

n = int(input())
result = 0

for i in range(1, n + 1):
    a = list(map(int, str(i)))
    sum_ = i + sum(a)

    if(sum_ == n):
        result = i
        break

print(result)
