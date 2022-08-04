import sys
input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]
result = []
for i in matrix:
    reverse_ = i[::-1]
    result.append(reverse_)
print(*result, sep='\n')