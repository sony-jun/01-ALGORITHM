t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    box = []
    for i in range(n):
        box.append(list(map(int, input().split())))

    move = 0
    for i in range(m):
        for j in range(n):
            for k in range(j + 1, n):
                if box[j][i] == 1 and box[k][i] == 0:
                    move += 1

    print(move)
