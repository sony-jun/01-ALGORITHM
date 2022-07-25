import sys

sys.stdin = open("1_상수.txt")
input = sys.stdin.readline

A, B = map(str, input().rstrip().split())
A, B = int(A[::-1]), int(B[::-1])

print(A) if A > B else print(B)