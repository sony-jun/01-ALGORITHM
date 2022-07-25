# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input()) #150 
b = int(input()) #266
c = int(input()) #427
# 곱한 정수 값은 str으로 바꾼뒤에 리스트로 만든다
result = list(str(a * b * c)) #[1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10): # i는 0~9까지 순회
    #정수 타입을 문자열 타입으로 바꾸는 이유는 cnt 함수 사용하기 위함
    print(result.count(str(i))) #i는 문자열 타입으로 바꿔서 count.