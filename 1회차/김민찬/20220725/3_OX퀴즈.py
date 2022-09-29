# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(T):
    count = 0
    sum = 0
    A = list(input())
    for i in A:
        if i == 'O': # 몇 번 'O'가 있는지 count
            count += 1
            sum = sum + count # 'O'일 때, 임의의 변수에 카운트 한 수를 더함
        else:
            count = 0 # 'X'일 때, 카운트한 수를 0으로 초기화
    print(sum)