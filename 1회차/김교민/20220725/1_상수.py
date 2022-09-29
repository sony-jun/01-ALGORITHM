# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(int, input().split())

a = (int(str(a)[::-1])) #두 정수 모두 문자열로 바꾸고 순서 바꾼 다음에
b = (int(str(b)[::-1])) #정수로 변환하기
if a > b:
    print(a)
else:
    print(b)