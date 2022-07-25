# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# input은 기본적으로 문자열 받음
a, b = input().split()
# 리스트 슬라이싱해서 숫자 거꾸로 나열
a = int(a[::-1])
b = int(b[::-1])

# 만약 a가 b보다 크면 a 출력
# 아니면 b출력
if a > b:
    print(a)
else:
    print(b)