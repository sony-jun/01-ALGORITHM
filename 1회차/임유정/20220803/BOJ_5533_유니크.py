#scrpit
import sys

# M: 가로 행
# N = 3 # 세로 열 고정
M = int(input())

card_matrix = [list(map(int, input().split())) for i in range(M)]

score_list = []
for j in range(3):
    temp_list = []
    
    for i in range(M):
        temp_list.append(card_matrix[i][j]) 
        
    score_list.append(temp_list)

for i  in range(M):
    result = 0
    for j in range(3):

        if score_list[j].count(card_matrix[i][j]) > 1:
            result += 0
        else:
            result += card_matrix[i][j]
    print(result)