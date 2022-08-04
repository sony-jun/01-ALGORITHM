n = int(input())
matrix = []
cnt_list = []

transposed_matrix = [[0] * n for _ in range(n)]
transposed_cnt_list = []

# matrix에 2차원 리스트 입력받기
for tc in range(n):
    room = list(input())
    matrix.append(room)

for i in range(n):
    # cnt 0으로 초기화
    cnt = 0
    for j in range(n):
        # 요소가 .이면
        if matrix[i][j] == ".":
            # cnt에 1씩 더하기
            cnt += 1
            # cnt_list에 cnt 추가
            cnt_list.append(cnt)
        # 요소가 X이면
        if matrix[i][j] == "X":
            # cnt 0으로 초기화
            cnt = 0
# cnt_list에서 요소가 2인 갯수 출력
print(cnt_list.count(2), end=' ')

# 원래 있던 리스트 전치시키기
for i in range(n):
    for j in range(n):
        transposed_matrix[i][j] = matrix[j][i]
        
# 위와 똑같은 과정 반복
for i in range(n):
    cnt = 0
    for j in range(n):
        if transposed_matrix[i][j] == ".":
            cnt += 1
            transposed_cnt_list.append(cnt)
        if transposed_matrix[i][j] == "X":
            cnt = 0
print(transposed_cnt_list.count(2))