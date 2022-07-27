n = int(input())
x = []
y = []
z = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
    
for j in range(n):
    
    if x[j] == max(x) and y[j] == max(y):
        z.append(1)
    elif x[j] == min(x) and y[j] == min(y):
        z.append(n)
    else:
        z.append(j)
print(z)
    


