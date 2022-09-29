len_a, len_b = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

both = set_a & set_b
# 입력받은 두 세트의 공집합 묶어줌
only_a = set_a - both
only_b = set_b - both
# 각 세트에서 공통된 부분 빼줌.
print(len(only_a) + len(only_b))
# 공집합을 뺀 집합의 길이를 각각 구하여 합해줍니다.