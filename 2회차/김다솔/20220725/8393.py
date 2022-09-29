# https://www.acmicpc.net/problem/8393

from unittest import result


n = int(input())
count = 0
for i in range(1, n+1):
    result = count + i
    print(sum(result))