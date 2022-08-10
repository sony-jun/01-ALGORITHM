n,m = map(int,input().split(' '))

notlistenlist = []
notsealist = []
notalllist = []
for i in range(n):
    notlistenlist.append(input())
for i in range(m):
    notsealist.append(input())

count = {}
for i in notlistenlist:
    try: count[i] += 1
    except: count[i] = 1
for i in notsealist:
    try: count[i] += 1
    except: count[i] = 1

for key,value in count.items():
    if value == 2 :
        notalllist.append(key)

print(len(notalllist))
for i in notalllist:
    print(i)