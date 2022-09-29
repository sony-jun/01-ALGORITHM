room = []
n = int(input())
for _ in range(n):
    room.append(list(input()))
col = 0
col_ = 0
for r in range(n):
    for c in range(1, n):
        # 앞과 뒤의 요소가 '.'이면 카운트.
        if room[r][c-1] == '.' and room[r][c] == '.':
            col += 1
        # 벽과 마주쳤을 경우, 그 전까지 카운트한 게 있으면 추가하고, 없으면 추가 안 함.
        elif room[r][c] == 'X':
            col_ += bool(col)
            col = 0
    # 벽과 마주치지 않고 끝났을 때 위 과정을 반복.
    col_ += bool(col)
    col = 0
row = 0
row_ = 0
for c in range(n):
    for r in range(1, n):
        if room[r-1][c] == '.' and room[r][c] == '.':
            row += 1
        elif room[r][c] == 'X':
            row_ += bool(row)
            row = 0
    row_ += bool(row)
    row = 0
print(col_, row_)