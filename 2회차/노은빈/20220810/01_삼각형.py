import sys
input = sys.stdin.readline

angles = [] #세 각의 값을 넣을 리스트

for _ in range(3): #삼격형 각 데이터를 세 번 받음
    angle = int(input())
    angles.append(angle) #리스트에 값 추가
# print(angles)


if sum(angles) == 180: #각의 합이 180도일 때
    if angles[0] == angles[1] == angles[2] == 60: #각의 값이 60도로 같을 때
        print('Equilateral')
    elif angles[0]  == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]: #세 각 중 두 각만 같을 때
        print('Isosceles')
    else : #같은 값이 없는 경우
        print('Scalene')
else : #세 각의 합이 180도가 아닐 때
    print('Error')
        
    
