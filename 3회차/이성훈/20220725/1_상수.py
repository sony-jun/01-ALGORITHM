# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

# 변수 A와 B에 문자 입력
A , B = input().split()
# A 와 B의 문자를 뒤집음(C와 D에 각각 넣음)
C = A[::-1]
D = B[::-1]
# C 와 D의 값을 상수로 변환
C = int(C)
D = int(D)
# C 와 D의 값을 서로 비교
# C 가 D보다 크거나 같을 경우 C출력
if C >= D:
    print(C)
else:
    print(D)

