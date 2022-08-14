# 10818.
"""
max() 와 min() 없이 구현해보기
"""
import sys
sys.stdin = open("최대최소.txt")

N = int(input())
numbers = list(map(int, input().split()))

big = 1
small = 1000000

for num in numbers:
    if big < num:
        big = num
    
    if small > num:
        small = num

print(small, big)