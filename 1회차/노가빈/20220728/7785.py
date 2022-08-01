t = int(input())
peopleList=[]
for i in range(t):
    people, ox = input().split(' ')
    if ox == 'enter':
        if people not in peopleList:
            peopleList.append(people)
    if ox == 'leave':
        if people in peopleList:
            peopleList.remove(people)
print(peopleList)