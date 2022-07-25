# https://www.acmicpc.net/problem/8958
import sys
from tempfile import tempdir

sys.stdin = open("3_OX퀴즈.txt")

time = int(input())
for t in range(1, time + 1):
    prob = input()
    total = 0
    q = 1
    for i in range(len(prob)):
        if prob[i] == 'O':
            if prob[i-1] == 'O' and (i != 0):
                q += 1
            else:
                q = 1
            total += q
    print(total)