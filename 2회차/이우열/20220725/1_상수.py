# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()                  # 입력 받은 두 개의 숫자를 문자열로 받는다

re_a = int(a[::-1])                     # 문자열을 뒤집은 후 숫자로 변환한다
re_b = int(b[::-1])

print(re_a if re_a > re_b else re_b)    # 두 수를 비교하여 최댓값을 출력한다
