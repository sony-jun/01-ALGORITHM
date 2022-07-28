# n = 4
# w = [[4,'misspell'],[1,'programming'],[7,'contest'],[3,'balloon']]
n = int(input())
w = []
r = []
for i in range(1,n+1):
    ota,word = input().split()
    ota = int(ota)
    w.append([ota,word])
for i in w:
    i[1] = list(i[1])
    del i[1][i[0]-1]
    i[1]=''.join(i[1])
    r.append(i[1])
for i in r:
    print(i)