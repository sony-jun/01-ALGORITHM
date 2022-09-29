import sys

sys.stdin = open("3_쉽게_푸는_문제.txt")

a, b = map(int, input().split())
list_ = []
sum_ = 0

for i in range(1, b+1):
    for j in range(i):
        list_.append(i)

for i in range(a-1, b):     
    sum_ += list_[i]
print(sum_)