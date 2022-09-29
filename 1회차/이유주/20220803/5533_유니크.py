from imp import C_BUILTIN


N = int(input())
num = [[], [], []]
for i in range(N): # 행
    a,b,c = map(int,input().split()) # 열
    num[0].append(a) #한플레이어의 1번째 점수
    num[1].append(b) #한플레이어의 2번째 점수
    num[2].append(c)

score = [0] * N
for i in range(3): 
    for j in range(N):
        if num[i].count(num[i][j]) >= 2: # 
            score[j] += 0
        else:
            score[j] += num[i][j]

for s in score:
    print(s)