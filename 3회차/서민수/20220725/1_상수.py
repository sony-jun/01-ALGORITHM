
# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("1_상수.txt")

# 두 수를 비교하기 위해 input 함수를 받는다
# 상수는 수를 거꾸로 읽는다 734는 437로 읽는다면 생각나는건 리스트 뒤집기 (::-1)
# 두 수를 비교해보자

# a,b를 받을 함수
a, b = input().split()

# 각 a와 b를 리스트로 뒤집어준 후 인트 형변환
a = a[::-1]
b = b[::-1]

# 만약 a가 b보다 크다면
if a > b:
    # a 출력
    print(a)
else:
    # 그렇지 않다면 b 출력
    print(b)
