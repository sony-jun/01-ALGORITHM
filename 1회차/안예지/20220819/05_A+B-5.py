# 10952
"""
"""
import sys
sys.stdin = open("더하기5.txt")

sum_ = 1
# 값을 초기화
while True:
    sum_ = sum(map(int, input().split()))
    if sum_ != 0:
        print(sum_)
    else:
        break