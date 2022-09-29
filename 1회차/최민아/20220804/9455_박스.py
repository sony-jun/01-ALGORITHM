import sys
sys.stdin = open("20220804/9455_박스.txt")

T = int(input())

for test_case in range(T):
    m, n = map(int, input().split())                    # 행, 열

    grid = []                                           # box가 놓여진 상황
    for i in range(m):
        grid.append(list(map(int, input().split())))    # 2차원 배열

    move = 0                                            # 이동거리
    for j in range(n):
        for i in range(m):                              # 열 순회
            if grid[i][j] == 1:                         # 박스를 발견하면
                for k in range(i+1, m):                 # 이후 공간들 중
                    if grid[k][j] == 0:                 # 비어있는 공간 만큼
                        move += 1                       # 이동거리 1증가
    
    print(move)                                         # 최종 이동거리 출력