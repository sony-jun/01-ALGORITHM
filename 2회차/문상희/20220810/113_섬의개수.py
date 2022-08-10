a, b = map(int, input().split())

while a != 0 and b != 0:
    mat = []
    for _ in range(b):
        line = list(map(int, input().split()))
        mat.append(line)
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    def search(x, y, mat):
        for _ in range(8):
            ni = di[_] + x
            nj = dj[_] + y
            if ni in range(b) and nj in range(a):
                if mat[ni][nj] == 1:
                    mat[ni][nj] = 0
                    search(ni, nj, mat)
    cnt = 0
    for i in range(b):
        for j in range(a):
            if mat[i][j] == 1:
                search(i, j, mat)
                cnt += 1
    
    print(cnt)

    a, b = map(int, input().split())