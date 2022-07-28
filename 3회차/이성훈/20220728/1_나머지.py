# https://www.acmicpc.net/problem/3052
import sys

sys.stdin = open("1_나머지.txt")

M_list = []

for i in range(10):
    N = int(input())
    M = N % 42
    M_list.append(M)

print(len(list(set(M_list))))