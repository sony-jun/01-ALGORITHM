lst = []
dic = dict()

for i in range(3):
    lst.append(int(input()))
    if lst[i] not in dic:
        dic[lst[i]] = lst[i]
    else:
        dic[lst[i]] += lst[i]
        
if len(dic) == 1 and sum(dic.values()) == 180:
    print('Equilateral')
elif len(dic) == 2 and sum(dic.values()) == 180:
    print('Isosceles')
elif len(dic) == 3 and sum(dic.values()) == 180:
    print('Scalene')
elif sum(dic.values()) != 180:
    print('Error')
