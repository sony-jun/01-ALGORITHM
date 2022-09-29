# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

l = [0]*10          # 리스트 10개 생성
d = a*b*c           # a,b,c 곱하기
for i in str(d):    # 문자열로 변환 후, 반복문
    l[int(i)] += 1  # 인덱싱으로 해당 값에 1씩 더함
for j in l:         # 리스트를 반복문으로 하나씩 출력
    print(j)