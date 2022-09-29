# 9455
# m행 n열로 이루어진 그리드가 주어진다
# 일부 칸에는 박스가 들어있다. 모든 박스가 더 이상 움직일 수 없을 때까지
# 아래로 움직인다면 박스는 쌓여진 상태가 된다
# 박스가 움직인 거리는 바닥에 쌓이기 전까지 이동한 칸의 개수
# 모든 박스가 이동한 거리(각 박스가 이동한 거리의 합)을 구하라

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다
# 각 테스트 케이스의 첫째 줄에는 m과 n이 주어진다
# 다음 m개 줄에는 그리드의 각 행의 정보를 나타내는 n개의 정수가 주어진다
# 그리드 첫 행부터 마지막 행까지 순서대로 주어진다
# 박스가 들어있는 칸은 1로, 없는 칸은 0으로 주어진다

import sys
sys.stdin = open('박스.txt')

for _ in range(int(input())):
    m, n = map(int, input().split())
    #* 열 별 상자의 위치를 저장한 이차원 리스트
    grid = [[] for _ in range(n)]

    #* 열 별 박스의 위치 저장
    for i in range(m):
        a = list(input().split())
        for j in range(n):
            grid[j].append(a[j])

    #* 모든 박스가 이동한 거리
    moveCnt = 0
    for i in range(n):
        #* i열의 박스의 개수
        boxNum = grid[i].count('1')
        #* 바닥 위치
        floor = m - 1

        #* 열의 아래부터 박스의 위치 이동
        for j in range(m - 1, -1, -1):
            #* 박스를 제자리에 놓고 바닥을 1 높임
            if grid[i][j] == '1':
                moveCnt += floor - j
                floor -= 1

    print(moveCnt)