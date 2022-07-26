# https://www.acmicpc.net/problem/2609

A, B = map(int, input().split())

for idx in range(min(A, B), 0, -1):
    min_ = 0
    max_ = 0
    if A % idx == 0 and B % idx == 0:
        min_ = idx
        max_ = (A * B) // idx
        break

print(min_)
print(max_)