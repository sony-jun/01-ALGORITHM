# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# 문자열 형태로 입력
a, b = input().split()

# 문자열을 뒤집고 숫자형으로 변환
a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

# 두 수를 비교하여 큰 수를 출력
if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)
