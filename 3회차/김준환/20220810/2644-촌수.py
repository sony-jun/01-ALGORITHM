from pprint import pprint

n, m = map(int,input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    matrix[x][y] = 1
pprint(matrix)
lst = []
print(lst)
for x in range(n+1):
    lst2 = []
    for y in range(n+1):
        if matrix[x][y] == 1:
            lst2.append(y)
    lst.append(lst2)
print(lst)