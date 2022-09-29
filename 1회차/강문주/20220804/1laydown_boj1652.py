N = int(input())
matrix = [list(map(str, input().strip())) for _ in range(N)]

row = 0
column = 0

for x in range(N): #행
    cnt = 0
    for y in range(N): #열
        if matrix[x][y] == '.': #[행]][열]
            cnt += 1
        elif matrix[x][y] == 'X':
            if cnt >= 2: #x만났을때 이미 2칸 있으면 cnt증가
                row += 1 
            cnt = 0
    if cnt >= 2: #가로가 두칸 이상이 되면 cnt증가
        row += 1
    cnt = 0

for y in range(N): #배열을 회전
    cnt = 0
    for x in range(N):
        if matrix[x][y] == '.':
            cnt += 1
        elif matrix[x][y] == 'X':
            if cnt >= 2:
                column += 1
            cnt = 0
    if cnt >= 2:
        column += 1
    cnt = 0

print(row, column) #누울 수 있는 행열값을 출력