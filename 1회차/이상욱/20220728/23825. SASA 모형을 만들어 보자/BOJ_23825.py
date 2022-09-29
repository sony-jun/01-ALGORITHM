import sys
sys.stdin = open ('23825.txt')

N, M = map(int,input().split())

print(min(N//2, M//2))