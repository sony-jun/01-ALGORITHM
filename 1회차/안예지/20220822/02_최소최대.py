# 10818
"""
"""
import sys
sys.stdin = open("최소최대.txt")

N = int(input())
number = list(map(int, input().split()))
max_ = -10000001
min_ = 10000001

for num in number:
    if num > max_:
        max_ = num
    
    if num < min_:
        min_ = num
        
print(min_, max_, sep=" ")