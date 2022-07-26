T = int(input())
b=list(map(int, input().split()))
c=[]
for i in range(T):
    if i == T-1:
        break
    if b[i] < b[i+1]:
        c.append(b[i])
        print(c)
    if b[i] > b[i+1]:
        pass
print(c)

