# N = int(input())
# bomb = [input() for _ in range(N)]
# game = [input() for _ in range(N)]



# for i in range(N-2+1):
#     for j in range(N-2+1):
#         if game[i][j] == 'x':
#             star = 0
#             for r in range(2):
#                 for c in range(2):
#                     if bomb[i+r][j+c] == '*' \
#                     or bomb[i-r][j+c] == '*' :
#                         star += 1
#             print(star)