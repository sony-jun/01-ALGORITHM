# 100X100의 2차원 리스트에 0으로 초기화
matrix = [[0] * 100 for _ in range(100)]

# 4번 반복
for i in range(4):
    # 좌표들 입력받기
    x1, y1, x2, y2 = map(int, input().split())

    # 결과 cnt 변수 생성
    cnt = 0

    # (x1, y1), (x2, y2)에 접근
    for i in range(x1, x2):
        for j in range(y1, y2):
            # 만약 값이 0이면(이미 1이면 바꾸지 않음)
            if matrix[i][j] == 0:
                # 1로 바꾸기
                matrix[i][j] = 1

    # matrix에 접근
    for i in range(100):
        for j in range(100):
            # 값이 1이면
            if matrix[i][j] == 1:
                # 1씩 더하기
                cnt += 1
print(cnt)