# # 1652.
# """
# 5
# ....X
# ..XX.
# .....
# .XX..
# X....

# """
from pprint import pprint
# N = int(input())
# room = []
# for row in range(N):
#     room.append(list(input()))
# # pprint(room)
# # 행 우선순회
# # 빈 칸의 개수 저장할 변수
# slot = 0
# ga_seat = 0
# se_seat = 0
# for r in range(len(room)):
#     for c in range(len(room[0])):
#         if room[r][c] == '.':
#             slot += 1
#         elif room[r][c] != '.':
#             if slot >= 2:
#                 ga_seat += 1
#                 slot = 0
#     if slot >= 2:
#         ga_seat += 1
#     slot = 0
# # X가 행에 하나도 없을 때
# # for row in room:
# #     if 'X' not in row:
# #         ga_seat += 1
        
# # 리스트의 [r]번째 인덱스에 'X'가 있는지 저장할 변수        
# X_count = 0
# for c in range(len(room[0])):
#     for r in range(len(room)):
#         if room[r][c] == '.':
#             slot += 1
#         elif room[r][c] != '.': 
#             if slot >= 2:
#                 se_seat += 1
#                 slot = 0
#                 X_count += 1
#             else:
#                 slot = 0
#     if X_count == 0:
#         se_seat += 1
#     slot = 0
# print(ga_seat, se_seat)

N=int(input())
a=[]
r=0
e=0
for i in range(N):
    b=list(input().rstrip()) #개행 제거
    a.append(b)
pprint(a)

for q in range(N):
     z=0
     x=0
     for w in range(N):
          if a[q][w]==".":#가로 x가 빈자리
               x+=1
          else:#0초기화
               x=0
          if x==2:
               r+=1
               
          if a[w][q]==".":#세로 z가 빈자리
               z+=1
          else:#0초기화
               z=0
          if z==2:
               e+=1

print(r,e)