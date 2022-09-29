# https://www.acmicpc.net/problem/1269

import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
amb = A - B
bma = B - A
result = 0

result = len(amb) + len(bma)

print(result)