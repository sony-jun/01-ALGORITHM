import sys
sys.stdin = open("2. 사분면.txt", "r")

input = sys.stdin.readline

Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0
T = int(input())

for _ in range(T):
    x , y = map(int,input().split())
    if x > 0 and y > 0 : # 둘다 양수 1사분면
        Q1 += 1
    elif x < 0 and y > 0 : # x만 음수 2사분면
        Q2 += 1
    elif x < 0 and y < 0 : # 둘다 음수 3사분면
        Q3 += 1
    elif x > 0 and y < 0 : # y만 음수 4 사분면
        Q4 += 1
    elif x == 0 or y == 0 : # 선에 걸친 것.
        AXIS += 1
print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')
    