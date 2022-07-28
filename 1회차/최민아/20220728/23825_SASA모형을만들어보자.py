import sys
sys.stdin = open("20220728/23825_SASA모형을만들어보자.txt")

N, M = map(int, input().split())

S2 = N//2
A2 = M//2

SASA = min(S2, A2)

print(SASA)