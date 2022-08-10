from pprint import pprint
import sys

sys.stdin = open('2669.txt')

n = 4

coor = [list(map(int, input().split())) for i in range(n)]
#pprint(coor)
r_max = 0
c_max = 0

for r in range(4):
    for c in range(0, 4, 2):
        #print(coor[r][c])
        if coor[r][c] >= c_max:
            c_max = coor[r][c]
#print(r_max)

for r in range(4):
    for c in range(1, 5, 2):
        #print(coor[r][c])
        if coor[r][c] >= r_max:
            r_max = coor[r][c]
#print(c_max)

matrix = [[0] * c_max for i in range(r_max)]
for r in range(r_max):
    for c in range(c_max):
        matrix[r][c] = [r, c]
pprint(matrix)

coor_list = []
for i in range(n):
    for r in range(coor[i][1], coor[i][3]):
        for c in range(coor[i][0], coor[i][2]):
            if matrix[r][c] not in coor_list:
                coor_list.append(matrix[r][c])
print(len(coor_list))

