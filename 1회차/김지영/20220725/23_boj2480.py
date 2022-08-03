n = list(map(int,input().split()))

for i in range(len(n)):
    if n[i] == n [i-1] == n[i-2] :
        print(n[i],n[i-1],n[i-2],10000+n[i]*1000,sep=' ')
        break
    elif (n[i] == n[i-1] or n[i] == n[i-2]) and n[i-1] != n[i-2]:
        print(n[i],n[i-1],1000+n[i]*100,sep=' ')
        break
    elif n[i] != n[i-1] and n[i] != n[i-2] and n[i-1] != n[i-2]:
        print(max(n),max(n)*100,sep=' ')    
        break
