# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# 정수 인풋 두개 거꾸로 만들고 비교 
# int(str(a)[::-1])
# https://docs.python.org/release/2.3.5/whatsnew/section-slices.html

a, b = input().split() # a, b = str
a_r = int(a[::-1])
b_r = int(b[::-1])
print(max(a_r, b_r))
# if a_r > b_r:
#     print(a_r)
# else:
#     print(b_r)

