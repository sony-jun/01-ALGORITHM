# https://www.acmicpc.net/problem/2908

#max 함수
#인자로 전달되는 객체의 최소, 최대값을 찾아 리턴합니다.

import sys
sys.stdin = open('1_상수.txt', 'r')

x, y = input().split()

reversed_x = x[::-1]
reversed_y = y[::-1]

print(max(reversed_x, reversed_y))