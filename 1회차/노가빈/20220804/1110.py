n = int(input())
if n < 10 :
    n = n*10

count = 0
templist = list(str(n))
if templist[0] == '0':
    templist.append('0')
while True:
    tempnum1 = int(templist[0]) + int(templist[1])
    tempnum1 = list(str(tempnum1))
    tempnum2 = int(templist[1] + tempnum1[-1])
    templist = list(str(tempnum2))

    
    if len(templist) == 1:
        templist.insert(0,'0')
    count += 1
    if tempnum2 == n :
        break
print(count)
