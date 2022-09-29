T = int(input())
people = []

for i in range(T):
    weight, height = map(int, input().split())
    people.append((weight, height))
#print(people)

rank = [0] * T
for i in people:
    for j in people:
        if i[0] > j[0] and i[1] > j[1]:
            rank[people.index(j)] += 1

for i in rank:
    print(i+1, end=" ")