li = []

for ii in range(9):
    li.append(int(input()))
li.sort()
sum = sum(li)
a = 0
b = 0
for i in range(9):
    for j in range(i+1,9):
        if sum - (li[i] + li[j]) == 100:
           a = li[i]
           b = li[j]
li.remove(a)
li.remove(b)
print('\n'.join(map(str,li)))