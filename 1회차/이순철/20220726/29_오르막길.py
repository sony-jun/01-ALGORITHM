# https://www.acmicpc.net/problem/2846
import sys

sys.stdin = open("29_오르막길.txt")

t = int(input())
for test_case in range(1, t + 1):
    high = input().split()
    cnt = 0
    nu = 1
    for i in (high):
        if int(i) == 'O':
            if ox[i-1] == 'O' and i != 0:
                nu += 1
            else:
                nu = 1
            cnt += nu
    print(cnt)