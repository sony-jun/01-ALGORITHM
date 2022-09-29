# 11021
""" 
"""
import sys
sys.stdin = open("더하기7.txt")

# T = int(input());print(*[f'Case #{t}: {sum(map(int, input().split()))}' for t in range(1, T + 1)], sep = '\n')

T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{t}: {A + B}')