import sys


sys.stdin = open("0_숫자의개수.txt")
lst = []
for i in range(3):
    k = int(input())
    lst.append(k)
mul = lst[0] * lst[1] * lst[2]
mul = str(mul)
dic = {}
for i in mul:
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1
print(dic)



