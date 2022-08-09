N=int(input())
ans=0

def find(i) :
    for s in str(i) :
        if s not in '47' :
            return False
    return True

for i in range(4, N+1) :
    if find(i) :
        ans=int(i)

print(ans)
