# https://www.acmicpc.net/problem/1292
# 쉽게 푸는 문제

# 풀이
A, B = map(int, input().split())
seq = []
sum_ = 0
N = 1

while len(seq) < B:
    for i in range(N):
        seq.append(N)
    N += 1

print(seq)

for j in range(A-1, B):
    sum_ += seq[j]

print(sum_)