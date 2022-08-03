n = int(input())
scores = [list(map(int,input().split())) for i in range(n)]
result = [0]*n
fst = []
snd = []
trd = []
for score in scores:
    fst.append(score[0])
    snd.append(score[1])
    trd.append(score[2])
for i in range(n):
    if fst.count(fst[i]) == 1:
        result[i]+=fst[i]
for i in range(n):
    if snd.count(snd[i]) == 1:
        result[i]+=snd[i]
for i in range(n):
    if trd.count(trd[i]) == 1:
        result[i]+=trd[i]
print(*result,sep='\n')