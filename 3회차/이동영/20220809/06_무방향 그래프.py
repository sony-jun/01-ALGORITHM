n, m = map(int, input().split())

a = [[0] * 7 for _ in range(n+1)]
list_ = [[] for _ in range(n+1)]

for _ in range(0,m):
    i, j = map(int, input().split())

    a[i][j] = 1
    a[j][i] = 1
    list_[i].append(j)
    list_[j].append(i)

for i in a:
    print(*i)

print(list_)