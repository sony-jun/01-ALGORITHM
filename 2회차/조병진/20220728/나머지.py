# 나머지
# 문제 : 42로 나눴을 때, 서로 다른 나머지가 몇 개인지 출력
# 접근 : 42로 나눈 나머지를 구하고, 중복 값을 제거해 남은 개수를 구함

arr = []
for i in range(10):
    n = int(input())
    n_ = n % 42
    arr.append(n_)

print(len(set(arr)))
