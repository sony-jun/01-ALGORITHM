# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
# 정수를 input으로 받음
for test_case in range(1, T+1):
    OX = input()
    count = 0
# OX에다가 정수를 받아서 1씩 더해서 카운트를 함
for i in OX:
    if i == 'O':
        count += 1
    else:
        i == 'X'
        count == 0

        break
# O 면 1을 더하고 X 면 0으로 냅두고 반복하여 카운트를 함 다 체크하면 break로 멈춤 
print(count)
# 코드결과 (잘못되었는지 틀렸다고 나옴..)