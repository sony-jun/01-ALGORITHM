# A / B 원소의 개수 입력 받기
A, B = map(int, input().split())

# A / B 모든 원소 입력 받기
A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

# A - B / B - A
one = A_set - B_set
two = B_set - A_set

# one, two 합집합의 개수 출력
print(len(one | two))