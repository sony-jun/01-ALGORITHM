from pprint import pprint
# matrix = [list(map(int,input().split())) for _ in range(3)]
# pprint(matrix)
n,m = map(int,input().split())
matrix = []
for _ in range(n):
    line = list(map(int,input().split()))
    matrix.append(line)
pprint(matrix)
    
