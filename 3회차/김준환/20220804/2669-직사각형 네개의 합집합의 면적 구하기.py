# from pprint import pprint
import sys
input = sys.stdin.readline

matrix = [[0]*10 for _ in range(10)]
# pprint(matrix)
for _ in range(4):                              # 4줄의 입력
    x1, y1, x2, y2 = map(int,input().split())   # x1, y1 => 사각형 왼쪽 아래
    for y in range(y1,y2):                      # x2, y2 => 사각형 오른쪽 위
        for x in range(x1,x2):              
            matrix[y][x] = 'X'                  # 해당되는 범위는 X로 치환
# pprint(matrix)
s=0                                             # 카운트 위한 초기값
for y in range(10):                             # 100까지 행 접근하여 열 리스트 안에서 x카운트
    s += matrix[y].count('X')                   
print(s)