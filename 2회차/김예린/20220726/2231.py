# 분해합

N = int(input())                        

for i in range(1, N + 1):               
    num_list = list(map(int, str(i)))   
    sum_ = i + sum(num_list)            
    if(sum_ == N):                      
        print(i)                        
        break                          
    elif i >= N:
        print('0')                        