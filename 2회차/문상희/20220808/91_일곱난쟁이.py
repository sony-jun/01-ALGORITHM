littles = []

for i in range(9):
    stature = int(input())
    littles.append(stature)

littles = sorted(littles)
lair = []

for i in range(9):
    for j in range(i + 1, 9):
        if (sum(littles) - littles[i] - littles[j]) == 100:
            lair.append([littles[i], littles[j]])


for i in littles:
    if i not in lair[0]:
        print(i)