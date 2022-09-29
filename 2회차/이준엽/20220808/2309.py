dwalfs = [] #난쟁이 빈리스트를 생성
for _ in range(9):
    dwalf = int(input())
    dwalfs.append(dwalf)
sum_d = sum(dwalfs)
f_dwalf = []

for i in range(8):
    for j in range(i+1,9):
        result = sum_d - (dwalfs[i]+dwalfs[j])
        if result == 100:
            f_dwalf.append(dwalfs[i])
            f_dwalf.append(dwalfs[j])
            break
    if result == 100:
        break
for k in f_dwalf:
    if k in dwalfs:
        dwalfs.remove(k)
print(*sorted(dwalfs),sep='\n')
