# 7568
T = int(input())
person= []
for test in range(1, T +1):
    kg, cm = map(int,input().split())
    person.append((kg,cm))


for i in person:
    rank = 1
    for j in person:
        if i[0] < j[0] and i[1] < j[1]:
            rank+= 1
    print(rank,end = ' ')
    
    