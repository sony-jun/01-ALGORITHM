# 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 
# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

matrix = []
for _ in range(8):
    line = list(input())
    matrix.append(line)

cnt_ = 0
for i in range(8): #행범위설정
    for j in range(8): #열범위설정 # 그 안에서
        if (i + j) % 2 == 0: #하얀칸일 경우 (2,2), (4,4)...
            if matrix[i][j] == 'F': #하얀칸 안에 F있을 경우
                cnt_ += 1
print(cnt_)