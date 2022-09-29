from ast import MatchValue


n1,n2 = input().split(' ')

for i in range(len(n1)):
    if n1[i] == '5':
        n1 = list(n1)
        n1[i] = '6'
        n1 = ''.join(n1)
for i in range(len(n2)):
    if n2[i] == '5':
        n2 = list(n2)
        n2[i] = '6'
        n2 = ''.join(n2)
maxvalue = int(n1) + int(n2)

for i in range(len(n1)):
    if n1[i] == '6':
        n1 = list(n1)
        n1[i] = '5'
        n1 = ''.join(n1)
for i in range(len(n2)):
    if n2[i] == '6':
        n2 = list(n2)
        n2[i] = '5'
        n2 = ''.join(n2)
minvalue = int(n1) + int(n2)

print(minvalue,maxvalue)