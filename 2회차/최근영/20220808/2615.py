matrix = [list(map(int,input().split())) for _ in range(19)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
one_cnt = 0
two_cnt = 0
one_index = []
two_index = []
x = 0
y = 0

for i in range(0,len(matrix)):
    for j in range(0,len(matrix)):
        if matrix[i][j] == 1:
            one_index.append((i,j))
        elif matrix[i][j] == 2:
            two_index.append((i,j))
print(one_index)
print(two_index)

for k in range(len(one_index)):
    for l in range(len(dx)):
        nx = one_index[k][0] + dx[l]
        ny = one_index[k][1] + dx[l]
        if (nx, ny) in one_index:
            one_cnt+=1
            nnx = nx + dx[l]
            nny = ny + dx[l]
            if (nnx, nny) in one_index:
                one_cnt+=1
                nnx = nnx + dx[l]
                nny = nny + dx[l]
                if (nnx, nny) in one_index:
                    one_cnt+=1
                    nnx = nnx + dx[l]
                    nny = nny + dx[l]
                    if (nnx, nny) in one_index:
                        one_cnt+=2
                        print(one_cnt)
                        exit(0)
                    else:
                        one_cnt = 0
                else:
                    one_cnt = 0
            else:
                one_cnt = 0
                
for p in range(len(two_index)):
    for q in range(len(dx)):
        tnx = two_index[k][0] + dx[q]
        tny = two_index[k][1] + dx[q]
        if (tnx, tny) in two_index:
            two_cnt+=1
            tnnx = tnx + dx[q]
            tnny = tny + dx[q]
            if (tnnx, tnny) in one_index:
                two_cnt+=1
                tnnx = tnnx + dx[q]
                tnny = tnny + dx[q]
                if (tnnx, tnny) in one_index:
                    two_cnt+=1
                    tnnx = tnnx + dx[q]
                    tnny = tnny + dx[q]
                    if (tnnx, nny) in one_index:
                        two_cnt+=2
                        print(two_cnt)
                        exit(0)
                    else:
                        two_cnt = 0
                else:
                    two_cnt = 0
            else:
                two_cnt = 0