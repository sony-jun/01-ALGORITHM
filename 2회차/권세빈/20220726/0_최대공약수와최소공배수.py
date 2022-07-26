# https://www.acmicpc.net/problem/2609
# 두 개의 자연수를 입력받아 
# 최대 공약수와 최소 공배수를 출력

a, b = map(int,input().split())

# 최대 공약수 구하기
max_ = 0
for i in range(1, min(a,b)+1):      # a,b 중 작은 수로 공통 약수 구하기
    if a % i == 0 and b % i == 0:   # 둘다 0으로 딱 떨어지는 약수
        max_ = i                    # 마지막 약수가 최대 공약수
min_ = a*b//max_    # a,b 곱한 값을 최대 공약수로 나눴을 때 
                    # 몫이 최소 공배수

print(max_)
print(min_)

# for j in range(max(a,b),(a*b)+1):
#     if j % a == 0 and j % b == 0:
#         min_ = j
#         break
# print(min_)