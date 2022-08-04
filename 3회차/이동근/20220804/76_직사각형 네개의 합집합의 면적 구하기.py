# 좌표로 구하는 방식을 참조
# https://velog.io/@holawan/%EB%B0%B1%EC%A4%80-2669%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95-%EB%84%A4%EA%B0%9C%EC%9D%98-%ED%95%A9%EC%A7%91%ED%95%A9%EC%9D%98-%EB%A9%B4%EC%A0%81-python

l = [[0 for _ in range(101)] for __ in range(101)]

max_x = 0
max_y = 0
for _ in range(4):
    line = list(map(int, input().split()))
   
    if max_x < line[2]:
        max_x = line[2]
    if max_y < line[3]:
        max_y = line[3]

    for i in range(line[0], line[2]):
        for j in range(line[1], line[3]):
            if not l[i][j]:
                l[i][j] = 1

ret = 0
for i in range(max_x):
    for j in range(max_y):
        if l[i][j]:
            ret += l[i][j]

print(ret)

# 아주 간결하고 좋다.
# 다만 최적화는 안되어 있다.
# https://www.acmicpc.net/source/47178912
# 
# area = [[0]*100 for _ in range(101)]

# for _ in range(4):
#     x1,y1,x2,y2 = map(int,input().split())

#     for i in range(x1,x2):
#         for j in range(y1,y2):
#             area[i][j] = 1

# print(sum(map(sum, area)))