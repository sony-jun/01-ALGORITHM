
numlist=[]
for i in range(1,1000):
    for n in range(i):
        numlist.append(i)

x,y=map(int,input().split())

sum_num=0

suma= sum(numlist[x-1:y])

print(suma)
# for number in range(numlist):
#     for nums in number
# for number in numlist(range(x,y+1)):
#     sum_num+= 

# print(numlist)
