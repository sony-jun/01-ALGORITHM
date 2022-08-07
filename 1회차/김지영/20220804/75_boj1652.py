n = int(input())
matrix = [list(input()) for _ in range(n)]
garo = 0
sero = 0
garo_lay = 0
sero_lay = 0
for y in matrix:
    # print(y)
    for x in y:
        if x == '.':
            garo += 1
        else:
            if garo > 1:
                garo_lay += 1
            garo = 0
    if garo > 1:
        garo_lay += 1
    garo = 0
# print(garo_lay)
for j in range(n):
    sero_list = [matrix[i][j] for i in range(n)]
    # print(sero_list)
    for x in sero_list:
        if x == '.':
            sero += 1
        else:
            if sero > 1:
                sero_lay += 1
            sero = 0
    if sero > 1:
        sero_lay += 1
    sero = 0
print(garo_lay,sero_lay)