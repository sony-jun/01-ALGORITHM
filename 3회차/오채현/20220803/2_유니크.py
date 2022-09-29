# n = int(input())

# scores = [list(map(int, input().split())) for _ in range(n)]

# n = 5
# m = 3

# scores = [
#     [100, 99 , 98],
#     [100, 97, 92],
#     [63, 89, 63],
#     [99, 99, 99],
#     [89, 97, 98],
# ]

# 각 열이 게임 수 3 으로 고정
# n = 플레이어 수 = 행의 갯수  => 행의 인덱스를 플레이어 번호로scores[0] ... scores[n]
#scores[i][j] for i in range(n) => 각 게임당 플레이어들이 제시한 점수 list

# ply = []
# for i in range(n):
    
    # print(list(scores[i][j] for j in range(m)))

# for i in range(n):
# for j in range(m):
#     ply.append([scores[i][j] for i in range(n)])
# print(ply)

# total_list = []

# for pl in ply:
#     total = 0
#     # print(pl)
#     for i in range(n):
#         # print(pl.count(pl[i]))
#         if pl.count(pl[i]) == 1:
#             total += pl[i]
#         total_list.append(total)
#     print(total_list)
# for t in total_list:
#     print(t)

    # if scores[i].count(scores[i][j]) == 1:
    # print(scores[i], scores[i][j])
# print([scores[i][j] for i in range(n)])

#-------------------
# 행, 열을 뒤집어서 받기 => 열 3 고정을 행으로 변경 받는 플레이어 수 = 열

n = 5 # len(scores)
m = 3

scores = [
    [100, 99 , 98],
    [100, 97, 92],
    [63, 89, 63],
    [99, 99, 99],
    [89, 97, 98],
]

# n = int(input())
# m = 3
# scores = [list(map(int, input().split())) for _ in range(n)] 

#일반적으로 받아서 뒤집기

ply = []
for j in range(m):
    ply.append([scores[i][j] for i in range(n)])

totalSum = []
for i in range(n):
    total = 0
    for j in range(m):
        if ply[j].count(ply[j][i]) == 1:
            total += ply[j][i]
    totalSum.append(total)

for t in totalSum:
    print(t)



