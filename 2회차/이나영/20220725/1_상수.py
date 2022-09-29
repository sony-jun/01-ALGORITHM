# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# 리스트 슬라이싱은 리스트변수[시작인덱스:종료인덱스:step]으로 이루어진다.
# step을 이용하면 함수를 이용하지 않고도 리스트의 내용을 뒤집을 수 있다.
# input받은 값을 거꾸로 돌려서 int로 변환.

a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)