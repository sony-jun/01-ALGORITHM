import random

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
n7 = int(input())
n8 = int(input())
n9 = int(input())
lst = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
r = []
while True:
    temp = random.choice(lst)
    if temp not in r:
        r.append(temp)
    if len(r) == 7:
        if sum(r) == 100:
            break
        else :
            r = []
r.sort()
for i in range(len(r)):
    print(r[i])