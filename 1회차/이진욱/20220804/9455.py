
T = int(input())

for t in range(T):

    N,M = map(int,input().split())

    S_list = [  list(map(int,input().split())) for _ in range(N)]

    cnt = 0

    for k in range(N): # 행의 개수만큼 반복
        for i in range(N-1,0,-1): # 맨 아래 행부터 올라간다.
            for j in range(M):
                if S_list[i][j] == 0 and S_list[i-1][j] ==1: # 자기자신이 0이고 윗 칸의 숫자가 1일때
                    S_list[i][j] = 1 #자기 자신을 1로 바꾸고
                    S_list[i-1][j] = 0 # 윗 칸의 숫자를 0으로 바꾼다.
                    cnt+=1 # 이동횟수를 카운트해준다.

    print(cnt)




# 1 1 1    1 1 1     0 0 0     0 0 0
# 1 1 0 -> 0 0 0 ->  1 1 1  -> 1 1 1
# 0 0 0    1 1 0     1 1 0     1 1 1