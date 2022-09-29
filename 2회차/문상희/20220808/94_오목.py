mat = []
for i in range(19):
    each = list(map(int, input().split()))
    mat.append(each)

di = [0, 1, 1, -1]
dj = [1, 1, 0, 1]

def omok():
    for i in range(19):
        for j in range(19):
            if mat[i][j] != 0:
                point = mat[i][j]
                for k in range(4):
                    cnt = 1
                    ni = i + di[k]
                    nj = j + dj[k]

                    while 0 <= ni < 19 and 0 <= nj < 19 and mat[ni][nj] == point:
                        cnt +=1
                        if cnt == 5:
                            if 0 <= (i - di[k]) < 19 and 0 <= (j - dj[k]) < 19 and mat[i - di[k]][j - dj[k]] == point:
                                break
                            if 0 <= (ni + di[k]) < 19 and 0 <= (nj + dj[k]) < 19 and mat[ni + di[k]][nj + dj[k]] == point:
                                break
                            return point, i + 1, j + 1
                        
                        ni += di[k]
                        nj += dj[k]
    
    return 0, -1, -1

color, i, j = omok()
if color != 0:
    print(color)
    print(i, j, end = ' ')
else:
    print(0)




