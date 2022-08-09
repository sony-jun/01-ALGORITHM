n,m=map(int,input().split())

C=list(map(int,input().split()))
result_list=[]
S=[]

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            result=C[i]+C[j]+C[k]
            result_list.append(result)


for i in result_list:
    if i<=m:
        S.append(i)
        
print(max(S))
