#부르트포스
t = int(input())
p = [] #input시킨 무게와 키를 넣어두는 곳
for case in range(t):
    #무게(x)와 키(y) 입력해서
    #p에 넣어둔다.
    x, y = map(int, input().split()) 
    p.append((x, y))
# p에 있는 서로 다른 값들 하나씩 비교를 하고
# 큰 값에 랭크를 1씩 더해준다.
for i in p:
    rank = 1
    for j in p:
        if i[0] < j[0] and i[1] < j[1]:
                rank+=1
    print(rank, end=' ')