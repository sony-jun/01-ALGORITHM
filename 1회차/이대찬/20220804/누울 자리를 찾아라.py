import sys

sys.stdin = open('누울 자리를 찾아라.txt')

N = int(input())

matrix = [list((input())) for _ in range(N)] #매트릭스 원소 입력
sum_R = 0
sum_C = 0

for r in range(0,N):  
    RT = 1
    CT = 1
    for c in range(1,N):  
        if RT ==1:
            if matrix[r][c-1] == '.' and matrix[r][c] == '.':
                sum_R += 1
                RT = 0
        if CT ==1:
            if matrix[c-1][r] == '.' and matrix[c][r] == '.':
                sum_C += 1
                CT = 0

print(sum_R, sum_C)
            
        
                
 
 
    
