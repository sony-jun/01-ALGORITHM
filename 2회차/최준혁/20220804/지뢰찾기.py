# 맨 처음 주어지는것 n = 지뢰찾기 맵의 크기(10보다 작거나 같음)
# 입력받은 n만큼 문자 개수를 입력 ex) n = 8 ........ 
# n개의 줄만큼 입력 ex) n = 8 8줄

# . = 클릭하기 전 필드 * = 지뢰 x = 사용자가 클릭한 필드
# 1. 지뢰가 있는곳을 클릭하면 출력 시 모든 지뢰가 보여야함
# 2. 지뢰가 없는곳을 클릭하면 열린 칸에는 0~8사이의 숫자가 출력되어야 함 -> 좌표


n = int(input()) # 8

mine_map = list(input() for _ in range(n)) # 지뢰를 입력할 리스트 # 64
mine_click = list(input() for _ in range(n)) # 사용자 클릭을 입력할 리스트 64
mine_result = [['.'] * n for _ in range(n)] # 결과를 출력할 리스트 64

# 열린 칸 주변에 지뢰가 몇개 있는지(열린칸에서 8방향을 탐색)
# ...
# .x.
# ...
dc = [-1, -1, -1, 0, 1, 1, 1, 0] # ex) -1,-1 = x보다 위,왼쪽 / -1,0 = x보다 위,중앙 
dr = [-1, 0, 1, 1, 1, 0, -1, -1] # -1,1 = x보다 위,오른쪽 / 0,1 = x보다 중앙,오른쪽


for c in range(n): # 세로
    for r in range(n): # 가로 
        # 지뢰를 밟지 않았을 경우
        if mine_map[c][r] == "." and mine_click[c][r] == "x": 
            # 클릭시 숫자를 뜨게하는 카운트
            cnt = 0
            # 클릭한 값(x)를 기준으로 8방위의 좌표를 확인 
            for k in range(8):
                nc = c + dc[k]
                nr = r + dr[k]
                # 좌표가 음수이거나(맵 밖을 벗어났거나), n보다 큰 경우 건너뜀
                if nc < 0 or nc >= n or nr < 0 or nr >= n:
                    continue
                # 좌표 안에 폭탄이 있을 경우
                if mine_map[nc][nr] == "*":
                    cnt += 1 # 숫자 카운트 증가(최대 8)
            # 클릭한 결과에 카운트를 저장한다 
            mine_result[c][r] = cnt

        # 지뢰를 밟았을 경우
        if mine_map[c][r] == "*" and mine_click[c][r] == "x":  
            for a in range(n):
                for b in range(n):
                    if mine_map[a][b] == "*":
                        mine_result[a][b] = "*"

#결과값 출력
for i in range(n):
    for j in range(n):
        print(mine_result[i][j], end='')
    print()


