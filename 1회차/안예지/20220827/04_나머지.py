# 3052
"""
"""
import sys
sys.stdin = open("나머지.txt")

answer = set()
for _ in range(10):
    answer.add(int(input()) % 42)
print(len(answer))