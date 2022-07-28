import sys

sys.stdin = open("2_나머지_input.txt")

# num을 담을 딕셔너리
count_ = {}

# 숫자 입력 받고 딕셔너리에 키값추가하고 그 val에 1 추가

for _ in range(10):
    num = int(input())
    count_[num % 42] = 1 # 서로 다 다른 값이 몇개인지가 궁금한거기 때문에 중복도 1로
#print(count_)

# 딕셔너리의 val값들을 모두 더해서 출력
ans = 0
for sum_ in count_.values():
    ans = ans + sum_
print(ans)