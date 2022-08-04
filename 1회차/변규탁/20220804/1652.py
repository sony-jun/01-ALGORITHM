N = int(input())
room = [list(input()) for _ in range(N)]

# 가로

bed_row = []
for i in range(N):
    count_ = []
    cnt = 0 
    for j in range(N):
        if room[i][j] != "X":
            cnt += 1
        else:
            count_.append(cnt)
            cnt = 0
    count_.append(cnt)
    bed_row.append([k for k in count_ if k >= 2])

# 세로
room_col = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(room[j][i])
    room_col.append(temp)


bed_col = []
for i in range(N):
    count_ = []
    cnt = 0
    for j in range(N):
        if room_col[i][j] != "X":
            cnt += 1
        else:
            count_.append(cnt)
            cnt = 0
    count_.append(cnt)
    bed_col.append([k for k in count_ if k >=2])


# bed_row/bed_col에서 2이상인 개수
row = 0
for i in bed_row:
    row += int(len(i))

col = 0
for i in bed_col:
    col += int(len(i))
   
print(row, col)