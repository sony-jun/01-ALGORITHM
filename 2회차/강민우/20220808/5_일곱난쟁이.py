people = []
for a in range(9):
    N = int(input())
    people.append(N)
    
total = sum(people)
no_people = set()
no1 = 0
no2 = 0
for a in range(8):
    for b in range(a+1,9):

        if total -(people[a] + people[b]) == 100:
            no1, no2 = people[a], people[b]
            break

people.remove(no1)
people.remove(no2)
people.sort()     

for a in people:
    print(a)



