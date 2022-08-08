# 오목

dx = [-1, 1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
omok = [list(map(int, input().split())) for _ in range(19)]
winner = 0
for a in range(19):
    for b in range(19):
        if omok[a][b] == 1:
            for c in range(8):
                cnt = 1
                if (19 > a + dy[c] >= 0) and (19 > b + dx[c] >= 0):
                    bx = b + dx[c]
                    ay = a + dy[c]
                    if omok[ay][bx] == 1:
                        cnt += 1
                        while True:
                            if (19 > ay + dy[c] >= 0) and (19 > bx + dx[c] >= 0):
                                if omok[ay + dy[c]][bx + dx[c]] == 1:
                                    ay += dy[c]
                                    bx += dx[c]
                                    cnt += 1
                                else:
                                    if cnt == 5:
                                        winner = 1
                                        print(winner)
                                        print(a + 1, b + 1)
                                        cnt = 1
                                        break
                            else:
                                break
                        if cnt == 5:
                            winner = 1
                            print(winner)
                            print(a + 1, b + 1)
        else:
            cnt = 1

        if omok[a][b] == 2:
            for c in range(8):
                cnt = 1
                if (19 > a + dy[c] >= 0) and (19 > b + dx[c] >= 0):
                    bx = b + dx[c]
                    ay = a + dy[c]
                    if omok[ay][bx] == 2:
                        cnt += 1
                        while True:
                            if (19 > ay + dy[c] >= 0) and (19 > bx + dx[c] >= 0):
                                if omok[ay + dy[c]][bx + dx[c]] == 2:
                                    ay += dy[c]
                                    bx += dx[c]
                                    cnt += 1
                                else:
                                    if cnt == 5:
                                        winner = 2
                                        print(winner)
                                        print(a + 1, b + 1)
                                        cnt = 1
                                        break
                            else:
                                break
                        if cnt == 5:
                            winner = 2
                            print(winner)
                            print(a + 1, b + 1)
        else:
            cnt = 1
if winner == 0:
    print(winner)