# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")


A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

total = A*B*C
total = str(total)
dict = {}
for j in range(0,10):
    dict[str(j)] = 0
for i in total:
    if i in dict:
        dict[i] += 1

for k in dict:
    print(dict[k])