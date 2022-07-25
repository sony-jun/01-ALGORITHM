# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split(" ")
A, B = A[::-1], B[::-1]
    
print(A if int(A) > int(B) else B)