import sys

sys.stdin = open("input.txt", "r")
n = int(input())

matrix = [ list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    score = 0
        
    for j in range(3):
        list_ = []    
        for k in range(n):
            list_.append(matrix[k][j])
             
        if list_.count(matrix[i][j]) == 1:
            score += matrix[i][j]

    print(score)

