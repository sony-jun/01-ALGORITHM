# https://www.acmicpc.net/problem/2851
import sys

sys.stdin = open("3.txt", "r")

n = []
sum_ = 0
for t in range(10):
    n.append(int(input()))

for i in n:
    sum_ += i
    if sum_ >= 100:        
        if sum_ - 100 > 100 - (sum_ - i):
            sum -= i
        break
print(sum_)


    
