# https://www.acmicpc.net/problem/1269

import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
amb = A - B
bma = B - A
result = []

result = set(amb + bma)

print(len(result))