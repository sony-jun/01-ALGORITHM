# 10871
"""
"""
import sys
sys.stdin = open("보다작은수.txt")

N, X = map(int, input().split())
num = input().split()
for _ in range(len(num)):
    if int(num[_]) < X:
        print(num[_], end = " ")