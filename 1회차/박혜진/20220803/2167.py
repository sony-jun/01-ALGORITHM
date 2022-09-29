# n x m 행렬 값 입력받기
n, m = map(int, input().split())

# n x m 2차원 행렬 입력받기
c = [list(map(int, input().split())) for _ in range(n)]

# 몇 번 반복할 건지 입력받기
a = int(input())

# 시작 열, 시작 행, 끝 열, 끝 행을 입력받기
for _ in range(a) :
    i, j, x, y = map(int, input().split())

    sum = 0

    # 시작 열부터 끝 열까지 
    for a in range(i-1, x) :
        # 시작 행부터 끝 행까지
        for b in range(j-1, y) :
            # 해당 인덱스 값을 더하기
            sum += c[a][b]

    print(sum)