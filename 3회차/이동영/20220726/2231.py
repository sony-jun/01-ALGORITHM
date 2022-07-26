N = int(input())
sum_list = []
bunhaehab_list = []

for i in range(1,N+1):
    sum_list.append(i)
    j = i
    
    while i > 0:
        sum_list.append(i%10)
        i //= 10
        
    if N == sum(sum_list):
        bunhaehab_list.append(j)
    else : 
        sum_list = []

if len(bunhaehab_list) == 0:
    print(0)           
else:
    print(min(bunhaehab_list))
        
    
                
    
    