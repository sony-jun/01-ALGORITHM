n = int(input())
result = {}
people = []
for i in range(n):
    name, log = input().split()
    result[name]=log
for i in result:
    if result[i] == 'enter':
        people.append(i)
people.sort(reverse=True)

for i in people:
    print(i)
