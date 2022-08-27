# 1764
"""
"""
import sys
sys.stdin = open("듣보잡.txt")

N, M = map(int, input().split())
hearing = [input() for _ in range(N)]
double = []
for _ in range(M):
    a = input()
    if a in hearing:
        double.append(a)


print(len(double))
print(*sorted(double), sep = '\n')
