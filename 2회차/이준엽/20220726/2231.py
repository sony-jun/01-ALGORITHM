n = int(input())
producer = []

for i in range(n):
    strnum = str(i)
    listnum = list(map(int,strnum))  #string도 iterable 하므로 list사용하지 않아도됨
    if i+sum(listnum) == n:
        producer.append(i)

if producer != []:
    print(min(producer))
else:
    print(0)

# listol = ['1','2','3','4']
# listol= list(map(int,listol))
# print(listol[0],type(listol[0]),sum(listol))