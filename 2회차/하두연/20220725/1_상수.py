# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt", "r")

a, b = map(str, input().split()) # 두개의 숫자를 문자열로 입력

a = int(a[::-1])    # 문자열을 뒤집은 후 숫자로 변환하고, 역순으로 출력
b = int(b[::-1])

if int(a) > int(b): # 두 수 최대값 비교 후 , a 입력값이 더 크면 출력.. 
    print(a)
else:
    print(b)
