n = int(input())
answer = []
for i in range(n):
    r,e,c = map(int,input().split())
    if r>e-c:
        answer.append('do not advertise')
    elif r<e-c:
        answer.append('advertise')
    else:
        answer.append('does not matter')
print(*answer,sep='\n')