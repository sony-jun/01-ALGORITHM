# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

case = int(input())

for i in range(case):
    ox = input() #ooxxoxxooo = 1+2+1+1+2+3 = 10
    result = 0
    is_o = 0
    for j in ox:
        if j == "O":
            is_o += 1 # 참이면 1씩 증가
            result = result + is_o # 1+2+3 ... 구현
        else:
            is_o = 0 # 거짓이면 is_o변수 초기화
            


    print(result)