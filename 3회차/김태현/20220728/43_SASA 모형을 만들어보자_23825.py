import sys
sys.stdin = open("43_SASA 모형을 만들어보자_23825.txt", "r")

# " S 2개 + M 2개가 1단위

N, M = map(int, input().split()) # N = S = 4, M = A = 5
print(min(N//2, M//2))