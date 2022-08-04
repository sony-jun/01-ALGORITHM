import sys
sys.stdin = open("3_박스.txt")


T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    #2차원 배열 형성
    arr = [list(map(int, input().split())) for _ in range(m)]
    

# 열 기준으로 위치 배열
    col_list = []
    for x in range(n):
        col = []
        for y in range(m):
            col.append(arr[y][x])
        #층을 세기 위해 역으로 바꿈
        col.reverse()
        col_list.append(col)

    cnt = 0
    for i in range(n):
        floor = 0
        for j in range(m):
            if col_list[i][j] == 1:
                cnt += floor - j
                floor += 1

    print(abs(cnt))

