# r,c = map(int,input().split())
# maps = [list(input()) for i in range(r)]

# dx = [1,1,0]
# dy = [0,1,1]

# cnt = 0
# result = []
# r_result = []
# for y in range(r):
#     for x in range(c):
#         if maps[y][x] == '.' or maps[y][x] == 'X':
#             cnt = 0
#             answer = 'yes'
#             if maps[y][x] == 'X':
#                 cnt+=1
#             for d in range(3):
#                 d_x = x+dx[d]
#                 d_y = y+dy[d]
#                 if not (0<=d_x<c and 0<=d_y<r):
#                     answer = 'no'
#                     break
#                 elif maps[d_y][d_x] == '#':
#                     answer = 'no'
#                     break
#                 if maps[d_y][d_x] == 'X':
#                     cnt+=1
#                     answer = 'yes'
#             if answer == 'yes':
#                 result.append(cnt)

# for i in range(5):
#     r_result.append(result.count(i))
# print(*r_result,sep='\n')

r,c = map(int,input().split())
list_ = []
for i in range(r):
    temp = list(input())
    list_.append(temp)
dc = [1,1,0]
dr = [0,1,1]
b_count_list = [0]*5
for y in range(r):
    for x in range(c):
        b_count = 0
        if list_[y][x] == '#':
            continue
        if list_[y][x] == 'X':
            b_count += 1
        for d in range(3):
            d_c = x+dc[d]
            d_r = y+dr[d]
            if not (-1<d_c<c and -1<d_r<r):
                break
            if list_[d_r][d_c] == '#':
                break
            if list_[d_r][d_c] == 'X':
                b_count+=1
        else:
            b_count_list[b_count]+=1
print(b_count_list)