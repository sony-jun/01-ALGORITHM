# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt")
a = int(input())
b = int(input())
c = int(input())

res = [0 for i in range(0, 10)]
num = a * b * c
while num:
    num, remainder = divmod(num, 10)
    res[remainder] += 1
for i in res:
    print(i)