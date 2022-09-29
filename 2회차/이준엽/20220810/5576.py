wuni = []
kuni = []
for _ in range(10):
    wuni.append(int(input()))
for _ in range(10):
    kuni.append(int(input()))
wuni.sort(reverse=True)
kuni.sort(reverse=True)
wscore = 0
kscore = 0
for i in range(3):
    wscore+=wuni[i]
    kscore+=kuni[i]
print(wscore,kscore)