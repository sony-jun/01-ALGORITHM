# https://www.acmicpc.net/problem/8958
# 연달아 나오는 경우 점수가 1점씩 증가
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(T):
    ox_list = list(input())
    score = 0 # 점수를 더하는데 사용
    sum_score = 0 #최종 더하는 값들을 변수에 저장
    for ox in ox_list: #입력값을 하나씩 꺼내서 ox변수에 넣고 if조건식을 이용 
        if ox == 'O': #0이 있으면 
             score += 1 #score 변수에 한개 추가 
             sum_score += score #sum에 score 추가되며 
        else:
            score = 0 #0없으면 score 0으로 리셋
    print(sum_score)

