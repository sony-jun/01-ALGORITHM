# n, m = map(int, input().split())

# #castle 리스트 만들기
# castle = [list(input()) for _ in range(n)]
# #
# r_cnt = 0
# c_cnt = 0
# #행에 x가 있는지 체크
# for i in range(n):
#     if 'x' not in castle[i]:
#         r_cnt += 1
#         print(castle[i])
# # # 행과 열을 체크
# for i in range(m):
#     c_check = False

#     for j in range(n):
#         #ij가 되면 0부터 4까지 열로움직이다. j가 먼저 증가하면 행이 밑으로 내려가게 된다.
#         if castle[j][i] == "X":
#             c_check = True
#     #check가 false이면 추가해주고
#     if c_check == False:
#         c_cnt += 1

# #둘중에 큰 값을 출력해준다.
# print(r_cnt if r_cnt > c_cnt else c_cnt)



n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row = [0] * n
col = [0] * m


for i in range(n):
    for j in range(m):
        if array[i][j] == "X" :
            row[i] = 1
            col[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

col_count = 0
for i in range(m):
    if col[i] == 0:
        col_count += 1
        
print(max(row_count, col_count))