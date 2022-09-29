import sys
sys.stdin = open('누울자리를찾아라_input.txt')

N = int(input())

# 방 정보 입력
room = []
for _ in range(N):
    room.append(list(input()))


ans = [0, 0] # 답
for i in range(N):
    row = 0 # 가로 경우
    col = 0 # 세로 경우
    for j in range(N):
        if room[i][j] == '.': # 행의 요소가 .일 경우 가로에 1추가
            row += 1
        elif room[i][j] == 'X': # 행의 요소가 X일 경우 가로가 2이상이면 정답에 1추가
            if row >= 2:
                ans[0] += 1
            row = 0 # 가로가 2이상이든 아니든 0으로 초기화
        
        if room[j][i] == '.': # 새로도 마찬가지
            col += 1
        elif room[j][i] == 'X':
            if col >= 2:
                ans[1] += 1
            col = 0
            
        if j == N-1: # 끝까지 갔을 때
            if row >= 2: # 가로가 2 이상이면  
                ans[0] += 1 # 정답에 1추가
            if col >= 2: # 새로가 2이상이면 
                ans[1] += 1 # 정답에 1추가
for a in ans:
    print(a,end=' ')
