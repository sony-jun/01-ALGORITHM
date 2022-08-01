N = int(input())

lst = []
for i in range(1, N+1):
    lst.append(i)

result = []

while(len(lst)>1):
    result.append(lst.pop(0))
    lst.append(lst.pop(0))
 
result.append(lst.pop(0))

for i in result:
    print(i, end=' ')