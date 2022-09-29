# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

multiply_abc = str(a * b * c)


for i in range(10):
    cnt = 0
    for char in multiply_abc:
        if int(char) == i:
            cnt += 1
    print(cnt)