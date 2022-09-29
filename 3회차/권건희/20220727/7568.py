A=['c=','c-','dz=','d-','lj','nj','s=','z=']
C=['č','ć','dž','đ','lj','nj','š','ž']
list_=[]
T=input()
cnt=0
for a in A:
    if a in T:
        bh=A.index(a)
        re=C[bh]
        rep=T.replace(a,re)

for c in C:
    if c in rep:
        list_.append(c)

for i in list_:
    print(type(i))
    if i in rep:
        rep=str(rep.lstrip(i))
print(type(rep))
               




       