# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

n1, n2 = input().split()            # 두 수를 문자열로 받음
if int(n1[::-1]) > int(n2[::-1]):   # 거꾸로 인덱싱 순서로 읽은 수를 정수형 변환 후
    print(n1[::-1])                 # 비교하여 큰 수 거꾸로 출력 그대로 프린트
else:
    print(n2[::-1])



