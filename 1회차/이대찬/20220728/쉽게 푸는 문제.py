lst = []

for i in range(1,100):
    for n in range(0,i):
        lst.append(i)
        if len(lst) > 1000:
            break
    if len(lst) > 1000:
            break

A,B = map(int,input().split(' '))

result = 0

while(A<=B):
    result += lst[A-1] 
    A += 1    

print(result)

        