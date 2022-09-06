from pprint import pprint
import sys


sys.stdin = open('1979.txt')

n , k = map(int , input().split())
mat = []
noin = 0
yein = 0
yein2 = 0
cnt = 0
cnt2 = 0
for _ in range(n):
    line = list(map(int , input().split()))
    mat.append(line)
# for x in range(n - k + 1):
#     for y in range(n - k + 1):
#         for j in range(5):
            
#             for i in range(y , y + k): 
                
            
            
#                 result = result + mat[j][i]
#             print(result)

#pprint(mat) 
for i in range(n):
    
    for y in range(n):
        
        if mat[i][y] == 1:
           yein = yein + 1
           

           if yein == 3 and y < n - 1:
                if mat[i][y + 1] != 1: 
                    cnt = cnt + 1
                      
           elif y == n - 1 and yein == 3 :
                

                cnt = cnt + 1

            
            
     
        
        elif mat[i][y] == 0:
             
             yein = 0

                
for y in range(n):
    
    for i in range(n):
        
        if mat[i][y] == 1:
            yein2 = yein2 + 1
            
            
     
        
        elif mat[i][y] == 1:
             
             yein2 = 0
        elif yein2 == 3 and mat[i+1][y] != 1:
            cnt2 = cnt2 + 1
                

print(cnt , cnt2)