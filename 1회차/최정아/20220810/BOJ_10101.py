# 삼각형의 세 각을 입력받음
angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
    if angle[0] == angle[1] == angle[2]: # 세 각의 크기가 모두 60이면
        print('Equilateral')
    # 세 각의 합이 180이고, 두 각이 같은 경우
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print('Isosceles')
    else: # 세 각의 합이 180이고, 같은 각이 없는 경우
        print('Scalene')
else: # 세 각의 합이 180이 아닌 경우
    print("Error")
