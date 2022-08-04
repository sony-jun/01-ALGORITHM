# from pprint import pprint

# T = int(input())

# for _ in range(T):
#     N, M = map(int,input().split()) 
#     matrix = [list(map(str, input().split())) for _ in range(N)] 

#     cnt = 0
#     pprint(matrix)
#     for y in range(5): # 0, 1, 2, 3, 4                                 
#         for x in range(4): # 0, 1, 2, 3
#             print(y, x)

#             if matrix[y][x] == "1":                                # 매트릭스를 순환하며 숫자가 1이 나오면  가로(x,y)의 y를 고정시킨후 x축만 for문을 돌린다 
    #             for i in range(y+1,len(matrix)):
    #                 if matrix[i][x] == "0":                        # for문을 돌며 세로로 내려가게하며 0이 나오면 움직여야하니 카운트에 1씩 더해준다.
    #                     cnt += 1
    # print(cnt)

#     matrix = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9, 0, 1, 2]
# ]

# for i in range(4): # 행
#   for j in range(3): # 열
#     print(matrix[j][i], end=" ")
#   print()