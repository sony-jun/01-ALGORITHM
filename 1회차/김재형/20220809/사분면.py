import sys
sys.stdin = open('사분면_input.txt')
# x가 0 이거나 y가 0이면 무조건 선위에
# x,y가 양수 1분면
# x가 음수, y가 양수면 2분면
# x,y 가 음수 3분면
# x가 양수, y가 음수면 4분면

# 점 개수
N = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
for n in range(N):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        axis += 1
    if x > 0 and y > 0:
        q1 += 1
    if x < 0 and y > 0:
        q2 += 1
    if x < 0 and y < 0:
        q3 += 1
    if x > 0 and y < 0:
        q4 += 1
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axis}')