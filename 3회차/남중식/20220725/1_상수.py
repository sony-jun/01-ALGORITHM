# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# 두 수를 반대로 읽는 상수의 대소 비교에 대한 답

A, B = map(int, input().split())

A_reverse = int(str(A)[::-1])
B_reverse = int(str(B)[::-1])

print(max(A_reverse, B_reverse))