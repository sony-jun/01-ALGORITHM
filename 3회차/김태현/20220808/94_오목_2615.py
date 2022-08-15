import sys
sys.stdin = open("94_오목_2615.txt", "r")

# 8방 델타 탐색
# 8방 내에 현재 위치랑 같은 값(1 or 2)이 있으면, 같은 방향으로 계속 탐색
# 5개 연속이면 승리, 6개 연속이면 pass
# 승리한 돌의 색, 첫번째 탐색 위치 출력

# -1 -1 /-1 0  / -1 1
# 0 -1  / 0 0  / 0 1
# 1 -1  / 1 0  / 1 1

# # 바둑판 매트릭스 생성
# badook = []
# for _ in range(19):
#     badook.append(list(map(int, input().split())))

# # 8방 델타값
# dx = [-1,-1,-1,0,0,0,1,1,1]
# dy = [-1,0,1,-1,0,1,-1,0,1]

# for i in range(1, 20):
#     for j in range(1, 20):

#         nx = i + dx
#         ny = j + dy
#         if 1 <= nx < 20 and 1 <= ny < 20:
#             if badook[nx][ny] == 1:
#                 True

print(bool(0))