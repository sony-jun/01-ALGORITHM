a, b = map(int,input().split())
s = []
for i in range(1,b+1):
    for j in range(i) :
        if len(s) == b :
            break
        s.append(i)
print(sum(s[a-1:b]))