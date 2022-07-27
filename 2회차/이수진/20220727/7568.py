n=int(input())
result=[]
answer=[]
for i in range(n):
    a,b=map(int, input().split())
    result.append([a,b])
for i in result:
    temp=0
    for j in result:
        if i[0] < j[0] and i[1] < j[1] :
            temp+=1
    answer.append(temp+1)

print(*answer)