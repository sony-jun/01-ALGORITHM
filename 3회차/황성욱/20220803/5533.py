import sys
# sys.stdin = open('./5533.txt')

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]

board = [0]*n # 점수를 합산하기 위해서 0 * 인원수
arr = []
for i in range(3): # 0, 1, 2 ~ 의 col 중에서
    temp = []
    for j in range(n): # 각 행의 0번쨰 요소 부터 리스트에 넣어줌
        temp.append(score[j][i])
    arr.append(temp)  # [, [99, 97, 89, 99, 97], [98, 92, 63, 99, 98]]
    
for i in range(n): # 인원수에 겹치는 값을 빼주기 위해서 
    for j in range(3):
        if arr[j].count(arr[j][i]) >= 2:  # [100, 100, 63, 99, 89] 중 겹치는 값이 있으면
            board[i] -= arr[j][i]        # borad 값에서 arr[j][i] 값을 빼줌

for i in range(3): # 각 열을 순회하면서
    for k in range(n): # board에 더해줌
        board[k] += score[k][i]

for res in board:
    print(res)