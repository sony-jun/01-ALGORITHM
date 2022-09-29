N = int(input())
room = [list(input()) for _ in range(N)]

# 가로

bed_row = []  

for i in range(N):
    count_ = [] 
    cnt = 1
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








# N = int(input())

# room = [list(input()) for _ in range(N)]

# 가로방개수 = [] # 답을 출력할때는 2이상인 요소가 들어가 있으니까 해당 길이를 출력.
#     # 가로방개수 - 2평의 이상의 방의 개수가 각 행의 정보에 들어가있음

# for i in range(N):
#     방갯수 = [] # i번째 의 방갯수 정보가 들어있음 i+1 번째가 되면
#     방의평수 = 0
#     for j in range(N):
#         if room[i][j] != 'X': # OOOXXXOO X를만 초기화해서 뒤에 O 누적합
#             방의평수 += 1
#         else:
#             방갯수.append(방의평수)
#             방의평수 = 0
    
#     방갯수.append(방의평수)
#     가로방개수.append([x for x in 방갯수 if x >=2])
        


# # 세로

# # 세로 방향을 다시 가로방향으로 바꿔야할것 같습니다.
# room2 = []
# for i in range(N):
#     temp = []
#     for j in range(N):
#         temp.append(room[j][i])
#     room2.append(temp)

# 세로방개수 = []

# for i in range(N):
#     방갯수 = [] # i번째 의 방갯수 정보가 들어있음 i+1 번째가 되면
#     방의평수 = 0
#     for j in range(N):
#         if room2[i][j] != 'X': # OOOXXXOO X를만 초기화해서 뒤에 O 누적합
#             방의평수 += 1
#         else:
#             방갯수.append(방의평수)
#             방의평수 = 0
    
#     방갯수.append(방의평수)
#     세로방개수.append([x for x in 방갯수 if x >=2])


# # 가로방갯수, 세로방갯수
# 가로 = 0
# for i in 가로방개수:
#     가로 += len(i)

# 세로 = 0       
# for i in 세로방개수:
#     세로 += len(i)


# print(가로, 세로)


