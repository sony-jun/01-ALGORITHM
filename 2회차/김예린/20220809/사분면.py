# 딕셔너리 접근 

t = int(input())
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 2
for _ in range(t):
    x, y = map(int, input().split())

    if x and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    else:
        Q4 += 1

print('#')