# 5533
"""
"""
from pprint import pprint

N = int(input())
matrix = [[100, 99, 98], 
         [100, 97, 92], 
         [63, 89, 63], 
         [99, 99, 99], 
         [89, 97, 98]]

# for _ in range(N):
#     matrix.append(list(map(int, input().split())))
# pprint(matrix)

# result = [[0] * len(matrix) for r in range(len(matrix[0]))]
result = [[0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0]]
for r in range(len(result)):
    for c in range(len(result[0])):
        result[r][c] = matrix[c][r]
"""====================================================="""
result = []
# 리스트를 90도 회전
for x in range(3): # matrix의 열 개수만큼 = result의 행 개수가 된다. 행을 만든다.
    col = [] # 열 리스트(result의 행 개수)
    for y in range(5): # matrix의 행 개수만큼 = result의 열 개수가 된다.
        col.append(matrix[y][x]) # 열 리스트의 요소 채우기(result의 행을 이루는 각 리스트에 요소 넣기)

    result.append(col) # 요소를 채워넣은 열 리스트를 전체 리스트(result)에 넣는다.
"""========================================================"""    

# pprint(result)
score_list = [0] * len(result[0])
for r in range(len(result)):
    for c in range(len(result[0])):
        # 한 행당 존재하는 점수의 개수가 1개일 때
        if result[r].count(result[r][c]) == 1:
            score_list[c] = result[r][c]
print(*score_list)

"""========================================================"""
score_list = [0] * 5
for x in range(3):
    col = result[x] # result의 x번째 리스트
    for y in range(5): # 그 안을 돌면서
        # 친구의 점수
        score = col[y] # 만나는 값(점수)들을 score 변수에 저장 < 변수 쪼개기 >
        
        # 친구의 점수가 리스트에서 1개일 때
        if col.count(score) == 1:
            # 친구의 점수가 증가합니다.
            score_list[y] += score
print(score_list)