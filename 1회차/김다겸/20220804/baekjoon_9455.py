t = int(input())

for tc in range(t):

    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]

    # 전치할 transposed_matrix 리스트에 0으로 초기화
    transposed_matrix = [[0] * m for _ in range(n)]

    # matrix를 전치
    for i in range(n):
        for j in range(m):
            transposed_matrix[i][j] = matrix[j][i]

    # cnt 변수 0으로 초기화
    cnt = 0

    # transposed_matrix 순회
    for i in range(n):
        # 바닥
        floor = m - 1

        # 바닥에서부터 순회
        for j in range(m-1, -1, -1):
            # 값이 1이라면
            if transposed_matrix[i][j] == 1:
                # 바닥 - 현재 위치
                cnt += floor - j
                # 바닥 1 높이기
                floor -= 1

    print(cnt)