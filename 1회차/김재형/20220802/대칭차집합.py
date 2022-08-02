# 집합 A의 원소 개수, B의 원소 개수
# A의 원소
# B의 원소
# A-B의 원소 개수 + B - A의 원소 개수

# 먼저 집합A 와 B의 개수를 입력 받는다.

a, b = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A+B 에서 A한번 뺴고 A+B에서 B한번 빼고 더하기
# A + B
for i in B:
    A.append(i)
A = set(A)
print(len(A)-a + len(A)-b)