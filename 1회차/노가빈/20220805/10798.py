lstlst = []
for i in range(5):
    lstlst.append(list(input()))
resultlist = []
c = 0
r = 0

for i in lstlst:
    if len(i) > r:
        r = len(i)

for i in range(r):
    for j in range(5):
        try:
            resultlist.append(lstlst[j][c])
        except:
            continue
    c += 1
print(''.join(resultlist))