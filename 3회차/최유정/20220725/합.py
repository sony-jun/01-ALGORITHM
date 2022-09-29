# https://www.acmicpc.net/problem/8393

from re import I


n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i
print(sum)