from re import L


n, m = map(int, input().split())

#castle 리스트 만들기
castle = [list(input()) for _ in range(n)]

r_cnt = 0
c_cnt = 0
#(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3)...
for i in range(n):
    if 'x' not in castle[i]:
        r_cnt += 1

# # i가 8이
# for i in range(m):
#     c_check = False

#     for j in range(n):
#         #ij가 되면 0부터 4까지 열로움직이다. j가 먼저 증가하면 행이 밑으로 내려가게 된다.
#         if castle[j][i] == "X":
#             c_check = True
    
#     if c_check == False:
#         c_cnt += 1

# # 
# print(r_cnt if r_cnt > c_cnt else c_cnt)

