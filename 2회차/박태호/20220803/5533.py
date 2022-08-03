# 유니크
# 같은 수가 없다면 자신이 가진 수를 하나 더 얻음
# 있다면 점수얻을수 없음
# 게임 3번함 얻은 점수의 총점 구하기
# 
# 100 99 98     0
# 100 97 92     92
# 63 89 63      215
# 99 99 99      198
# 89 97 98      89
from pprint import pprint
n = int(input()) 
# matrix = 
matrix = [list(map(int, input().split())) for _ in range(n)]
# print(matrix)
score = []
# for _ in range(n):
for i in range(3):
    result = []
    li = []
    for j in range(n):
        li.append(matrix[j][i]) #n 번째 요소들 
    # print(li,type(li)) #[100, 100, 63, 99, 89]
    
    for i in range(len(li)):
        cnt = []
        for j in range(len(li)):
            if li[i] == li[j]:
                cnt.append(j)  # 인덱스 번호 알아내서
                # print('cnt',cnt)
                # print(li)
        if len(cnt) > 1:
            for x in cnt:
                li[x] = 0                   
#     print(li)
    score.append(li)
# print(score)

for j in range(n):# 5
    ff = []
    for i in range(3):
        ff.append(score[i][j])
    print(sum(ff))

# score
# [0, 0, 63, 99, 89]
# [0, 0, 89,  0,  0]
# [0,92, 63, 99,  0]





