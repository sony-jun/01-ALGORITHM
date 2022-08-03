# N = int(input())
# game = [list(map(int, input().split())) for _ in range(N)]

# print(game)

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]

for i in range(N): # N의 범위동안
    sum = 0 # 합계를 낼 변수
    check = 1 # 
    for j in range(3):
        for k in range(N):
            if k == i:
                continue
            if game[k][j] == game[i][j]:
                check = 0 
                break
        if check == 1:
            sum += game[i][j]
    print(sum)