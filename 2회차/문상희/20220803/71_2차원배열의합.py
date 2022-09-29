hang, yeol = map(int, input().split())
metrix = [list(map(int, input().split())) for _ in range(hang)]



for _ in range(hang):
    s1, f1, s2, f2 = map(int, input().split())

    result = 0

    for i in range(s1 - 1, s2):
        for j in range(f1 - 1, f2):
            result += metrix[i][j]
    print(result)
