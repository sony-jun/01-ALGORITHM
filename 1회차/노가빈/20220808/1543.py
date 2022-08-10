str = input()
surchstr = input()
c = 0 
while True:
    if str.find(surchstr) >= 0:
        temp = str.find(surchstr)
        c += 1
        str = list(str) 
        del str[temp:temp+len(surchstr)]
        str = ''.join(str)
    if str.find(surchstr) < 0:
        break
print(c)