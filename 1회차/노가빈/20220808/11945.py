from pprint import pprint

n,m = map(int,input().split(' '))
lst = []
result = []
for i in range(n):
    lst.append(list(map(int,input())))
for i in range(n):
    lst[i].reverse()
    result.append(lst[i])
for i in range(n):
    resultstr = ''.join(str(s) for s in result[i])
    print(resultstr)