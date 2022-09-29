# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()
a = int(a[::-1]) #문자열을 해당 인덱스로 호출하면 문자열 뒤집은 결과 반환 후 정수 처리 
b = int(b[::-1])

if a > b:
    print(a)
else : 
    print(b)

