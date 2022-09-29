# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input()) # a,b,c 값 받음

d = list(str(a * b * c)) # 곱한값을 문자열로 바꾸고 리스트화

for i in range(0,10) :
    print(d.count(str(i))) # i 값에 0부터 9까지 넣으며 d에서 등장한 횟수 확인