# https://www.acmicpc.net/problem/8958
from re import A
import sys

sys.stdin = open("3_OX퀴즈.txt")

n = int(input()) 

for i in range(n):
    a = input() #O,X의 값을 받아주는.
    score = 0 # 점수
    cnt = 0 # 연속된 0 의 갯수
    for i in range(len(a)): #길이만큼 반복.
        if a[i] == 'O': #O일 경우 +1을 해주고
            cnt += 1
            score += cnt
        if a[i] == 'X': #X의 경우 초기화 해줌
            cnt = 0
    print(score)