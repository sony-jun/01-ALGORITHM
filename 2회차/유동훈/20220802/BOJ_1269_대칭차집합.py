# https://www.acmicpc.net/problem/1269
# 대칭 차집합

# 풀이
N, M = input().split()

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = list(set(A) - set(B)) + list(set(B) - set(A))
print(len(result))
