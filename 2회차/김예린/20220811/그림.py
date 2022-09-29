# 1926
# 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
# 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
# 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 

'''
input =
    6 5
    1 1 0 1 1
    0 1 1 0 0
    0 0 0 0 0
    1 0 1 1 1
    0 0 1 1 1
    0 0 1 1 1

output = 
    4
    9
'''
n, m = map(int, input().split())
painting = []

# 1.델타값 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

drawing_paper = []
painting = []
painting_cnt = 0

for _ in range(n):
    temp_list = list(map(int,input().split()))
    drawing_paper.append(temp_list)

    
# 2.이차원 리스트 순회
for x in range(n):
    for y in range(m):
        if drawing_paper[x][y] == 1:      # 1일때만 탐색을 수행한다. 

            # 3.델타값을 이용해 상하좌우 이동
            for i in range(4):
                painting.clear()
                nx = x + dx[i]
                ny = y + dy[i]

                while True:
                    if not(-1 < nx < n and -1 < ny < n):                # 인덱스 조건, 범위를 벗어나면 탈출
                        break
                    if (drawing_paper[x][y] == 0):  # 이동 시 0이면 탈출
                        painting.clear()
                        break
                    
                    painting.append(drawing_paper[x][y])
                    if painting.count(1) >= 2:
                        painting_cnt += 1

                    # 같은 방향 다음 좌표를 탐색
                    ny = ny + dy[i]
                    nx = nx + dx[i]

print(painting_cnt)
                    
