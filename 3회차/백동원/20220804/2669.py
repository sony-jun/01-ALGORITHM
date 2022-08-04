# 직사각형 네개의 합집합의 면적 구하기
from collections import deque

squares = deque([list(map(int, input().split())) for _ in range(4)])
총넓이 = 0
X = 0
for 사각형 in squares:
    총넓이 += (사각형[2] - 사각형[0]) * (사각형[3]- 사각형[1])
for a in squares:
    for b in squares:
        if (max(a[0], b[0]) < min(a[2], b[2])) and (max(a[1], b[1]) < min(a[3], b[3])):
            X += (min(a[2], b[2]) - max(a[0], b[0])) * (min(a[3], b[3]) - max(a[1], b[1]))

for 사각형 in squares:
    X -= (사각형[2] - 사각형[0]) * (사각형[3]- 사각형[1])
    
X /= 2
총넓이 -= int(X)

for c in range(4):
    list_ = squares.popleft()
    one = []
    two = []
    three = []
    four = []
    for _ in range(3):
        one.append(squares[_][0])
        two.append(squares[_][2])
        three.append(squares[_][1])
        four.append(squares[_][3])
    if (max(one) < min(two)) and (max(three) < min(four)):
        총넓이 += (min(two) - max(one)) * (min(four) - max(three))    
    squares.append(list_)

A = []
B = []
C = []
D = []
for _ in squares:
    A.append(_[0])
    B.append(_[2])
    C.append(_[1])
    D.append(_[3])
if (max(A) < min(B)) and (max(C) < min(D)):
    총넓이 -= (min(B) - max(A)) * (min(D) - max(C))
print(총넓이)