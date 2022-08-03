N, M = map(int, input().split())
castle = [list(map(str, input())) for _ in range(N)]
cnt1 = 0
cnt2 = 0

for n in range(N): # 세로
    if "X" not in castle[n]: # n : 0, 1, 2
        print(castle[n])
        cnt1 += 1

for m in range(M): # 가로
    # 각 행과 열마다 X가 들어있지 않는 행, 열의 개수를 구한다
    if "X" not in [castle[n][m] for n in range(N)]: # n :0, 1, 2 m : 0 
        cnt2 += 1                                   # n :0, 1, 2 m : 1
                                                    # n :0, 1, 2 m : 2
# 그 중 큰 값을 출력 
print(max(cnt1, cnt2))

# n = 세로
# m = 가로 

# [['.', '.', '.'] # [0]: [0, 1, 2]
#  ['.', '.', '.'] # [1]: [0, 1, 2]
#  ['.', '.', '.']]# [2]: [0, 1, 2]