from pprint import pprint
import sys

x,y = map(int,input().split(' '))
tempboxlist = []

input = sys.stdin.readline
for _ in range(x):
    tempboxlist.append(list(map(int,input().split(' '))))

boxlist = []
for i in range(y):
    templist = []
    for j in range(x):
        templist.append(tempboxlist[x-j-1][i])
    boxlist.append(templist)

i = 0
j = 0
count = 0
breakcount = 0
while True:
    if boxlist[i][j] == 0 and boxlist[i][j+1] == 1:
        boxlist[i][j] == 1
        boxlist[i][j+1] == 0
        count += 1
        
    else:
        breakcount += 1
    j += 1
    if i == y-1 and j == x-2:
        i = 0
        j = 0
        breakcount += 1

    if j == x-2:
        j =0
        i += 1
    if breakcount == 100:
        break
    


pprint(count)
