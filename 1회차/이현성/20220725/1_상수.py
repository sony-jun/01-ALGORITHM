# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(int,input().split()) # a와 b를 공백으로 나눠서 int로 받는다

a = list(str(a)) # int'a'를 문자열로 바꾼 후 리스트로 바꿔서 a로 저장
a.reverse() # 리스트 a 를 reverse 함수를 써서 거꾸로 
a = ''.join(a)
print(type(a))
b =list(str(b))
b.reverse()
b = ''.join(b)

if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print('error')