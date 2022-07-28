num = int(input()) 

result = {(0,0):1}
for i in range(0, num):
    a,b = map(int,input().split(' '))
    for i in list(result.keys()):
        result[(a,b)] = 0
        if i[0]<a and i[1]<b:
            result[(a,b)] = result[i] 
            result[i] = result[i] + 1 
        elif i[0]>a and i[1]>b:
            result[(a,b)] = result[i]  +1
        else:
            result[(a,b)] = result[i]

del result[(0,0)]

for i in result:
    print(result[i],end=" ")
    
#1 1 2 = 2
    

# a = {(1,2):1, (1,3):2}

# for i in a:
#     print(i)
# print(len(a))

# result = {(1,2):0,(2,3):0,(3,5):0,(6,7):0}

# a= list(result.keys())
# print(a[0])