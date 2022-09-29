# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())
mul_num = str(A * B * C)
check_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(mul_num)):
    check_list[int(mul_num[i])] += 1
for j in range(10):
    print(check_list[j])