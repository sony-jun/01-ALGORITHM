# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(str, input().split())

#문자열 a, b를 역순으로 재 할당 및 int형 형변환
# int형 변환 -> 수의 크기 비교를 위해
a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)