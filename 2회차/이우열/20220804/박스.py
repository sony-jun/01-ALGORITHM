t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    box = []
    for i in range(n):
        box.append(list(map(int, input().split())))

    re_box = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(box[j][i])
        re_box.append(temp)

    move = 0
    for i in range(m):
        for j in range(n):
            for k in range(j + 1, n):
                if re_box[i][j] == 1 and re_box[i][k] == 0:
                    move += 1

    print(move)
