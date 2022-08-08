from re import A
import sys
sys.stdin = open("합집합의 갯수구하기.txt")


matrix = [[0 for _ in range(100)] for _ in range(100)]
# 아, 이게 이중리스트고 행 100, 열 100으로 된 이중리스트구나.
# x,y가 100개씩 생긴 이중리스트. 눈금같은거지. 

for _ in range(4): #4개의 직사각형을 돌고
    x1,y1,x2,y2 = map(int, input().split()) # x1,x2,y1,y2에 저장
    for i in range(x1,x2): #x1,y1 를 돌면서 값을 입력시키고
        for j in range(y1,y2): #x2,y2를 돌면서 값을 입력시키다가
            if matrix[i][j] == 1 : #만약에 matrix(100,100)에 값이 있으면 계속 가고
                continue
            else :
                matrix[i][j] =1 #아니면 1씩 입력시킨다.

result = 0
for i in range(100): #100개의 좌표를 돌면서 입력시킨 값을 찾아서
    for j in range(100):
        if matrix[i][j] == 1: #입력되어있으면 
            result += 1 #변수에 1을 더해.
print(result)

#이차원배열을 다시 이해하느라 어제 수업 다시 들었고
#input값을 x1,x2,y1,y2로 받는데 for문 돌때 x1,y1 / x2,y2로 돌아야하는 이유를 찾으라 한참걸렸다.

# 솔비님처럼 생각할 수 없었던 이유가, 중복값을 제거해야 한다고 생각한거 같은데..좀 더 파이썬적인 생각이 필요해보인다.

# ### 와, 솔비님꺼 엄청 간단하다....# 대박사건,
# paper = [[0] * 101 for _ in range(101)]

# for _ in range(4):
#     x1, y1, x2, y2 = map(int,input().split())

#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             paper[i][j] = 1

# answer = 0

# for i in paper:
#     answer += sum(i)
    
# print(answer)