# https://www.acmicpc.net/problem/2908
# import sys

# sys.stdin = open("1_상수.txt", "r")

A, B = input().split()

A = A[::-1] # 역순으로 정렬
B = B[::-1]

print(max(A, B))