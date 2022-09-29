
from pprint import pprint


#word = input()
matrix = [list(input()) for _ in range (len(input()))]
#a = '.'
#b = 'x'
cnt = 0

#pprint(matrix)

for i in range(len(input())):
#    line = list(input())
#    matrix.append(line)

    if matrix[i][i] != 'X':
        cnt += 1
    #else: break

print(cnt)
