# import sys

# sys.stdin = open("_4396.txt", "r")


# N = int(input())
# bomb = [input() for _ in range(N)]
# game = [input() for _ in range(N)]

# answer = []

# for i in range(1, N):
#     temp = []
#     for j in range(1, len(bomb[0])):
#         if game[i-1][j-1] == 'x':
#             cnt = 0
#             for r in range(2):
#                 for c in range(2):
#                     if 8 > i - r > 0 and 8 > j - c > 0: 
#                         if bomb[i-1+r][j-1+c] == '*':
#                             cnt += 1
#                         elif bomb[i-1+r][j-1-c] == '*':
#                             cnt += 1
#                         elif bomb[i-1-r][j-1-c] == '*':
#                             cnt += 1
#                         elif bomb[i-1-r][j-1+c] == '*':
#                             cnt += 1
#                         elif bomb[i-1-r][j-1+c] == '*':
#                             cnt += 1
#                         elif bomb[i-1+r][j-1-c] == '*':
#                             cnt += 1
#                         elif bomb[i-1+c][j-1+c] == '*':
#                             cnt += 1
                  
                    
#             temp.append(cnt)
#     answer.append(temp)

# for g in answer :
#     print(g)