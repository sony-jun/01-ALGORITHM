import sys

sys.stdin = open('오목.txt')

matrix = [list(input().split()) for _ in range(19)]

델타_y = [-1, -1, -1, 0, 0, 1, 1, 1]
델타_x = [-1, 0, 1, -1, 1, -1, 0, 1]

T = 1
for x in range(19):
    for y in range(19):
        if matrix[x][y] == "1" or matrix[x][y] == "2":
            for d in range(8):
                탐색_x = x + 델타_x[d]
                탐색_y = y + 델타_y[d]
                if (탐색_x < 0  or 탐색_y < 0 
                    or 탐색_x > 18 or 탐색_y> 18):
                    continue
                if matrix[x][y] == matrix[탐색_x][탐색_y]:
                    cnt = 0
                    for i in range(1,4):
                        오목_x = 탐색_x + 델타_x[d]*i
                        오목_y = 탐색_y + 델타_y[d]*i 
                        if (오목_x < 0  or 오목_y < 0 
                            or 오목_x > 18 or 오목_y> 18):
                            continue
                        if matrix[탐색_x][탐색_y] == matrix[오목_x][오목_y]:
                            cnt +=1
                        else:
                            break
                        
                    if cnt == 3:
                        print(matrix[x][y])
                        print(f'{x+1} {y+1}')
                        T=0
        if T ==0:
            break
if T == 1:
    print('0')
                
       
                    
                  
                    
                        
                            
                        
                        
                        
                        
                
                
                    
            