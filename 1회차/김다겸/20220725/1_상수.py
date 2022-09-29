# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# a, b를 문자열 형태로 리스트로 저장
a, b = list(input().split())

# a, b 리스트의 요소를 뒤집어서 join을 통해 요소 연결
a_rev = ''.join(reversed(a))
b_rev = ''.join(reversed(b))

# 만약 a_rev가 b_rev보다 크다면
if a_rev > b_rev:
    # a_rev 출력
    print(a_rev)
else:
    print(b_rev)