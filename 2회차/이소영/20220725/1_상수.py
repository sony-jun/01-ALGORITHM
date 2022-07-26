# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split()

# 두 수를 역순으로 뒤집는다 
A_reverse = int(A[::-1])
B_reverse = int(B[::-1]) 

if A_reverse > B_reverse:
    print(A_reverse)
else:
    print(B_reverse)