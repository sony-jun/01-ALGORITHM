# 하얀 칸 / 체스판 => 하얀 칸 위에 말이 몇개 있는지? 
# 1. 행렬의 크기가 미리 주어지는(결정 된) 경우 == 8*8 행렬 생성 => 0으로 초기화하는 것으로! 
# 2. f 말이 들어간 상태를 표시
# 3. 말판이 메트릭스로 표현
# 4. 규칙 찾기: 흰색은 인덱스 두개 더하면 짝수, 검은색은 두개 더하면 홀수
# 1) 일단 초기화 한 후 입력 값 넣음
# 2) 

matrix = []

for _ in range(8):
    line = list(input())
    matrix.append(line)

# matrix = [list(input()) for _ in range(8)]

answer = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:  # 햐안 칸일 경우 짝수인 것을 표현
            if matrix[i][j] == 'F': #
                answer += 1

print(answer)
