# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
#연속으로 정답이 점수가  1씩증가

T=int(input())
a= 'O'#정답
b= 'X'#오답
score=0

d=0
z=0
x=0
N=input()# 정답오답 입력
list(N)
print(N, sep='')
