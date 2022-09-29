import sys
sys.stdin = open("1. 삼각형 외우기.txt", "r")
input = sys.stdin.readline

result = []
for _ in range(3):
    n = int(input())
    result.append(n)
if sum(result) != 180:
    print('Error') # 합이 180 아니면 'Error
else:
    if result[0] == 60 and result[1] == 60 and result[2] == 60:
        print('Equilateral') # result의 0,1,2번째 요소가 다 60이면 'Equilateral'
        
    elif sum(result) == 180 and result[0] == result[1] or result[1] == result[2] or result[0] == result[2] :
        print('Isosceles') # 합이 180이고 세 개중에 2개가 같으면. 'Isosceles'
        
    elif sum(result) == 180 and result[0] != result[1] or result[1] != result[2] or result[0] != result[2] :
        print('Scalene') # 합이 180이고 전부 다르면. 'Scalene'

    
    