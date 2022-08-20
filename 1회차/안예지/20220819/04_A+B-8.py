# 11022
""" 
"""
import sys
sys.stdin = open("더하기8.txt")

T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{t}: {A} + {B} = {A + B}')