# 누울 자리를 찾아라

n = int(input()) # 방의 크기 입력 받음

matrix = [] # 배열 넣을 빈 리스트 생성 

for _ in range(n): # n번 반복하여 입력 받고, 
    line = list(input()) # 리스트로 입력 받고  
    matrix.append(line) # 매트릭스 리스트 안에 리스트로 추가


answer = [0, 0] # 값 출력 리스트 생성
for i in range(n): # n 번 반복(가로)
    row = 0 # 가로 카운트 할 변수 생성
    col = 0 # 세로 카운트 할 변수 생성
    for j in range(n): # # n 번 반복(세로)
        # 가로
        if matrix[i][j] == '.': #(0,0)이 .이면 row에 일단 저장해야 하기 때문에 1추가
            row += 1
        else: # 연달아 나와야 하기 때문에 중간에 .이 아니면 0으로 초기화해야 됨
            row = 0
        if row == 2: #row가 2이면 누울 수 있기 때문에 answer0 인덱스에 1 추가, 2개이상이면 누울 수 있기 때문에 한줄 당 두개로 카운팅
            answer[0] += 1
        
        # 세로
        if matrix[j][i] == '.': # 0,0 일때 
            col += 1 # 1 추가 
        else:
            col = 0
        if col == 2: # col이 2이면 누울 수 있기 때문에 answer1 인덱스에 1 추가, 2개이상이면 누울 수 있기 때문에 한줄 당 두개로 카운팅
            answer[1] += 1
print(*answer)


        
