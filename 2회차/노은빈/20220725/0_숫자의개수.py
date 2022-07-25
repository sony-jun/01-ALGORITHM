# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a = int(input())
b = int(input())
c = int(input())

m = a* b* c
result = list(str(m))  #곱한 값을 문자열로 변환 후에 list
for i in range(10):  #리스트는 0부터 인덱스로 저장 i=0~9
    print(result.count(str(i)))  #i를 문자열로 바꾸고 count함수를 이용해 문자 개수 세기