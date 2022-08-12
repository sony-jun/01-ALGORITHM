# 트럭 미해결
import sys
sys.stdin = open('2979.txt')
A, B, C = map(int, input().split())
min_ = []
max_ = []

for _ in range(3):
    a, b = map(int, input().split())
    min_.append(a)
    max_.append(b)

list_ = [0] * (max(max_) + 2)

for i in range(3):
    for j in range(min_[i], max_[i] + 1):
        list_[j] += 1

result = (list_.count(1)) * A + (list_.count(2)-1) * B * 2 + (list_.count(3)) * C * 3
print(result)
print(list_)