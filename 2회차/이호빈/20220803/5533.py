n = int(input())

card = [list(map(int, input().split())) for i in range(n)]

r_card = []
score = [0 for _ in range(n)]


for i in range(3):
    s = []
    for j in range(n):
        #행먼저 증가해서 3*5에서 5*3이 된다.
        s.append(card[j][i])
    r_card.append(s)


for i in range(3):
    for j in range(n):
        #열 기준으로 점수를 저장했다. 
        if r_card[i].count(r_card[i][j]) == 1:
            #열 기준의 인덱스를 점수 기준으로 했다.
            score[j] += r_card[i][j]


for i in range(n):
    print(score[i])