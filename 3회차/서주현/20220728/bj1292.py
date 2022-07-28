from re import L
import sys

sys.stdin = open('bj1292.txt', 'r')  

a, b = list(map(int, input().split()))
result = 0

for i in range(a, b+1) :
    sum_ = 0
    for j in range(b+1) :
        sum_ += j
        # print(sum_, i, end= '//')
        if sum_ >= i :
            num = j
            break
    result += num
    
print(result)