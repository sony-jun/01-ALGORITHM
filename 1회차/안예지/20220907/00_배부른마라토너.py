# 10546
"""
"""
import sys
sys.stdin = open("마라토너.txt")

N = int(input())
loop = 2 * N - 1 
names = {}

for _ in range(loop):
  key = input()
  names[key] = names.get(key, 0) + 1

for key in names:
  if names[key] % 2 == 1:
    print(key)
