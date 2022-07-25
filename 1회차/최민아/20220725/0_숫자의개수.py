# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("20220725/0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
cnt = [0] * 10

for i in range(len(cnt)):
    for num in result:
        if int(num) == i: 
            cnt[i] += 1
    print(cnt[i])
