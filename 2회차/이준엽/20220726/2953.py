result = []
for i in range(5):
    a,b,c,d = map(int,input().split())
    result.append(a+b+c+d)
print(result.index(max(result))+1,max(result))