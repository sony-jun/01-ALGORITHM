# https://www.acmicpc.net/problem/2897

import sys
sys.stdin = open('B2897.txt')

R, C = map(int, input().split())
P = [list(input()) for _ in range(R)]
# print(P)
zero = 0
one = 0
two = 0
three = 0
four = 0
# destroy = [0] * 5
for i in range(R-1):
    for j in range(C-1):
        temp = []
        for x in range(2): # 첫번째 인덱스 기준으로 4칸
            for y in range(2):
                temp.append(P[i+x][j+y])
        if '#' not in temp: #건물이 차범위 안에 없으면 
            if temp.count('X') == 0:
                zero += 1
            elif temp.count('X') == 1:
                one += 1
            elif temp.count('X') == 2:
                two += 1
            elif temp.count('X') == 3:
                three += 1
            else:
                four += 1
print(zero, one, two, three, four, sep = '\n')