# https://www.acmicpc.net/problem/5533

import sys
sys.stdin = open('1.txt', 'r')
# from pprint import pprint

import sys
input = sys.stdin.readline

# 사람 수
n = int(input())
# 점수들 입력 받기
p = [list(map(int,input().split())) for _ in range(n)]

# 중복된 점수를 빼서 새로 담을 리스트
score = [[0]*3 for l in range(n)]

# 한 열을 game 리스트로 묶어줌
for j in range(3):
    game = [p[i][j] for i in range(n)]

    # 한 게임 중에서 점수가 하나만 있는 것만 score 리스트에 추가
    for k in range(n):
        if game.count(game[k]) == 1:
            score[k][j] = game[k]

# 리스트안에 리스트를 합산해서 출력
for h in score:
    print(sum(h))


