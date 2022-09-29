# 23253.
"""

"""
import sys
sys.stdin = open("자료구조.txt")

N, M = map(int, input().split())
last = []
for i in range(M):
    n = int(input())
    number = list(map(int, input().split()))
    for j in range(n):