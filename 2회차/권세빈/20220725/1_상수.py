# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()
# 문자열로 인풋 받기
print(max(int(a[::-1]),int(b[::-1])))
# 거꾸로 하고 정수형으로 변환, max로 최대값 구하기

