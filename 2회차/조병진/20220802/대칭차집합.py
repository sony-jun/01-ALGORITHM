# 대칭 차집합
# 문제 : A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.
#       예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때,  A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a - b) + len(b - a))
