# https://www.acmicpc.net/problem/8958
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. 
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성
import sys

sys.stdin = open("3_OX퀴즈.txt")

result = int(input()) 

for i in range(result):
    a = input() # oxoxxox...

    score = 0 # 점수
    count = 0 # 연속된 'O'의 개수

    for i in range(len(a)): # oxoxxox... 길이만큼 반복문
        if a[i] == 'O': 
            count += 1 
            score += count # 최종 점수에 더해줌
        if a[i] == 'X':
            count  = 0 
    print(score) # 점수를 출력