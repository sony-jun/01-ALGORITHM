# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

N = int(input())

for i in range(N):
    val = input()

    result = 0
    count = 0 
    for j in val:
        if j == 'O':
            count += 1
        else:
            result += count * (count + 1) // 2
            count = 0

    if count > 0:
        result += count * (count + 1) // 2

    print(result)
