# 10816
"""
"""
import sys
sys.stdin = open("숫자카드2.txt")

N = int(input())
sang = input().split()
sang_dict = {}
for cnt in sang:
    sang_dict[cnt] = sang_dict.get(cnt, 0) + 1

M = int(input())
numbers = input().split()
for num in numbers:
    print(sang_dict.get(num, 0), end = " ")
        
        