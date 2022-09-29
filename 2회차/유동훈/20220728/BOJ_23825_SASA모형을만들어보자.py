# https://www.acmicpc.net/problem/23825
# SASA 모형을 만들어보자

# 풀이
N, M = map(int, input().split())

if N/2 >= M/2:
    print(int(M/2))
else:
    print(int(N/2))