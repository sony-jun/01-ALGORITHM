import sys
sys.stdin = open('하얀칸.txt')

from pprint import pprint

matrix = [list(input())for _ in range(8)]
#pprint(matrix)
cnt = 0
for m in range(8):
    for n in range(8): 
        if (m + n)%2 == 0 and matrix[m][n] == 'F':
            cnt += 1
            #matrix[m][n] = 'W'
#pprint(matrix)
print(cnt)
