
A,B=map(int,(input()).split())
C = []
for i in range(1, B + 1):
    for j in range(i):       
        C.append(i)
print(sum(C[A-1:B]))#3부터 7까지 합15