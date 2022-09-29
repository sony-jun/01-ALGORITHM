import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
# 2차원 리스트 입력받기
paper = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    # 전역 변수 cnt 생성
    global cnt
    # 탐색할 때마다 cnt에 1 더하기
    cnt += 1
    # 현재 값을 0으로 바꾸기
    paper[x][y] = 0

    # 4방위 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 판을 나가지 않고 탐색한 다음 값이 1이면
        if -1 < nx < n and -1 < ny < m and paper[nx][ny] == 1:
            # 탐색한 다음 값으로 dfs 탐색 재귀
            dfs(nx, ny)


# cnt 값을 넣을 리스트 생성
num_list = []

# paper 순회
for i in range(n):
    for j in range(m):
        # paper 값이 1이면
        if paper[i][j] == 1:
            # cnt 0으로 초기화
            cnt = 0
            # i, j에 대해 dfs 탐색
            dfs(i, j)
            # 탐색이 끝난후 cnt 값을 리스트에 저장
            num_list.append(cnt)

# 만약 cnt가 추가 안되있으면
if len(num_list) == 0:
    print(len(num_list))
    # 0 출력
    print(0)
else:
    # cnt 개수 출력
    print(len(num_list))
    # cnt 중 가장 큰 수 출력
    print(max(num_list))