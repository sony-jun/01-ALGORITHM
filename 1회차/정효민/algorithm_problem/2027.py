from pprint import pprint


n = 5
m = 5
mat = []


for i in range(n):
    mat.append(['+'] * 5)
        
        
for x in range(n):
    for y in range(m):
        if x == y:
            mat[x][y] = '#'
for i in mat:
    print(*i)
    