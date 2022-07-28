import sys
sys.stdin = open("1_SASA모형을만들어보자.txt")

N, M = map(int, input().split())

common = min(N, M)

print(common // 2)
