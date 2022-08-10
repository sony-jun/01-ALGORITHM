# 조건 1. 세각의 합이 180
# 조건 2. 세각의 크기가 모두 60이면 eq~
# 조건 3. 세각 중 두 각이 같으면 is~
# 조건 4. 세각이 모두 다르면
# 조건 5. 세각 합이 180이 아니면

triangle = set()
equilateral = 0
sum_ = 0
for a in range(3):
    angle = int(input())
    if angle == 60:
        equilateral += 1
    if equilateral == 3:
        print('Equilateral')
    
    triangle.add(angle)
    sum_ += angle
if sum_ == 180:
    if len(triangle) == 2:
        print('Isosceles')
    if len(triangle) == 3:
        print('Scalene')
else:
    print('Error')