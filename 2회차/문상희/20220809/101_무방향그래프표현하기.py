import pprint

vertex, edges = list(map(int, input().split()))
gragh = []
matrix = []
for i in range(vertex + 1):
    line = []
    gragh.append([])
    for j in range(vertex + 1):
        line += [0]
    matrix.append(line)
for edge in range(edges):
    i, j = list(map(int, input().split()))
    gragh[i].append(j)
    gragh[j].append(i)
    matrix[i][j] = 1
    matrix[j][i] = 1

pprint.pprint(matrix)
print(gragh)