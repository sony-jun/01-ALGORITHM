sublist = list(map(int,input().split(' ')))
numlist = [1,1,2,2,2,8]

for i in range(6):
    if sublist[i] != numlist[i]:
        sublist[i] = numlist[i] - sublist[i]
    else:
        sublist[i] = 0
print(sublist)