# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

#print(int(str(a)[::-1]))
# 숫자a를 문자열a로 변환하여 리버스하고 다시 숫자로 변환
a, b = input().split()
c = int(a[::-1]) #문자열을 받아서 자리를 바꾼후 숫자로 변환
d = int(b[::-1])

if c > d :
    print(c)
else:
    print(d)