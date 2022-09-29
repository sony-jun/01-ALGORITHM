n = int(input())
info = []
#입력 받기
for i in range(0,n):
    tmp = list(map(int,input().split()))
    info.append(tmp)

print(info) 
    
    
for i in range(0,n):
    cnt = 1
    for j in range(0,n):
        check0 = (info[i][0] > info[j][0])
        check1 = (info[i][1] > info[j][1])
        
        if check0 and check1 :
            cnt+=1
        
        
    print(cnt, end = " ") 
