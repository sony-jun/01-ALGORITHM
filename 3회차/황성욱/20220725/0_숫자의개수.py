# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a = int(input())
b = int(input())
c = int(input())

m_val = str(a*b*c)
li = [0 for x in range(10)]

for num in m_val:
    li[int(num)] += 1

for i in li:
    print(i)
