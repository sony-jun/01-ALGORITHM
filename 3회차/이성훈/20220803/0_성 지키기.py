# https://www.acmicpc.net/problem/1236
import sys

sys.stdin = open("0_성 지키기.txt")

N , M = map(int,input().split())

r_count, c_count = 0, 0

matrix = [list(input()) for _ in range(N)]              # 행에 X가 없는지 조사
for i in range(N):
    if "X" not in matrix[i]:                            # 행에 X가 없으면 행 숫자 1증가
        r_count += 1


# for j in range(M):                                    # 아래처럼 푸는법 모르겠습니다.
#     for i in range(N):
#         if "X" not in matrix[i][j]:
#             c_count += 1
# print(max(r_count,c_count))


for j in range(M):                                      # 열에 X가 없는지 조사
    if "X" not in [matrix[i][j] for i in range(N)]:    # 열에 X가 없으면 행 숫자 1증가
        c_count += 1                                    

print(max(r_count,c_count))                             # 모든 행과 열에 적어도 1명 경비원을 채우려면 max 사용