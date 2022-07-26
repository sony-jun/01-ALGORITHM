# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수

# 풀이
A, B = map(int, input().split())

# 최대 공약수
for i in range(A, 0, -1):
    if A % i == 0 and B % i == 0:
        print(i)
        break
# 최소 공배수
for i in range(1, B + 1):
    if A * i % B == 0:
        print(A * i)
        break


