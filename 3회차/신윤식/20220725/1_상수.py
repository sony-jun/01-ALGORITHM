# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("./3회차/신윤식/20220725/1_상수.txt")

A, B = input().split()  # 문자열로 받음
A_R = int(A[::-1])      # 슬라이싱을 이용하여 문자열 순서를 뒤집고 숫자로 전환
B_R = int(B[::-1])

if A_R > B_R:           # 더 큰 값 대소비교
    print(A_R)
else:
    print(B_R)

# print(A_R) if A_R > B_R else print(B_R)