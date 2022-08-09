# 몬스터 트럭

R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
result = [0] * 5
dx = [1, 0, 1]
dy = [0, 1, 1]
for x in range(R - 1):
    for y in range(C - 1):
        tem_list = []
        tem_list.append(matrix[x][y])
        for a in range(3):
            lx = x + dx[a]
            ly = y + dy[a]
            tem_list.append(matrix[lx][ly])
        if '#' not in tem_list:
            cnt = tem_list.count('X')
            result[cnt] += 1
for results in result:
    print(results)

# R, C = map(int, input().split())
# matrix = [list(input()) for _ in range(R)]
# result = [0] * 5
# dx = [1, 0, 1]
# dy = [0, 1, 1]
# for x in range(R - 1):
#     for y in range(C - 1):
#         cnt = 0
#         if matrix[x][y] != '#':
#             switch = True
#             if matrix[x][y] == 'X':
#                 cnt += 1
#             for a in range(3):
#                 lx = x + dx[a]
#                 ly = y + dy[a]
#                 if matrix[lx][ly] != '#':
#                     if matrix[lx][ly] == 'X':
#                         cnt += 1
#                 else:
#                     switch = False
#                     break
#             if switch == True:
#                 result[cnt] += 1
# for results in result:
#     print(results)
