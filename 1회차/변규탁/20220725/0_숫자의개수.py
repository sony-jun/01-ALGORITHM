# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

number = str(A*B*C)

num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for num in number:
    num_list[int(num)] += 1

for num in num_list:
    print(num)


