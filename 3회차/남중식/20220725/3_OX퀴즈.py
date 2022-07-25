# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(T):
    case = input()
    
    # count : O가 연속될 때 점수가 올라가는 것을 체크하기 위함
    count = 0
    
    # result : 총점을 계산하기 위함
    result = 0
    for c in case:
        # 현재 문자가 X면 o에 대한 count를 0으로 만듬
        if c == 'X':
            count = 0   
        # 현재 문자가 o면 o에 대한 count를 올리고 총점에 더함
        elif c == 'O':
            count = count + 1
            result = result + count
    print(result)
    
