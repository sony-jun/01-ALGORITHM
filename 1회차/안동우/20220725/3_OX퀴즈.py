# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
#연속으로 정답이 점수가  1씩증가
#'O'문자열로 보고 문제에 문자열 80까지
#문자열비교


T=int(input())

for z in range(1,T+1):
    a,b=0,1
    s=list(input())
    for j in s:
        if j=='O':
            a+=b#점수합 a저장
            b+=1#문제 점수처럼 1씩증가
        else:
            b=1#X가 나오면 1로 초기화  0의점수가 1이라
    print(a)
