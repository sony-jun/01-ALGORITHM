# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# a b 를 입력 받는다.
a, b = input().split()

# [::-1]은 단순하게 문자열을 뒤집어 준다.
a = a[::-1]
b = b[::-1]

# 뒤집은 값을 다시 저장해주고, max를 이용하여 더 큰값을 출력한다.
print(max(a, b))
