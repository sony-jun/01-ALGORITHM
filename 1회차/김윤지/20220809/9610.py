
n = int(input())

q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

for _ in range(n):
    x, y = map(int,input().split())
    if x == 0 or y == 0: # 하나라도 0이면 axis에 더하기
        axis += 1
    elif  x > 0 and y > 0: #둘다 양수면 q1에 더하기
        q1 += 1
    elif x < 0 and y > 0 : # x는 음수, y는 양수면 q2에 더하기
        q2 += 1
    elif x < 0 and y < 0 : # x,y 둘다 음수면 q3에 더하기
        q3 += 1
    else:  # 나머지는 q4에 더하기
        q4 += 1
print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)

