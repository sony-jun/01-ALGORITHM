# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())
d = list(str(a * b * c))

print(d)
for i in range(0,10) :
    print(d.count(str(i)))