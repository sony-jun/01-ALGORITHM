# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(str, input().split())

a = a[::-1] # 정수를 리스트로 형변환후 슬라이싱으로 뒤집기
b = b[::-1]

list_1 = ''.join(a) # 리스트형식을 join 함수로 연결하여 출력
list_2 = ''.join(b) 


if list_1> list_2:
    print(list_1)
else:
    print(list_2)


