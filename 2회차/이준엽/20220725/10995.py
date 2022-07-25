k = int(input())

for i in range(1,k+1):
    sumstar=''
    for j in range(1,k+1):
        sumstar+='* '
    if i%2 == 0:
        print(' '+sumstar)
    else:
        print(sumstar)