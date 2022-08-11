lst = []
for i in range(1,6):
    man = input()
    if 'FBI' in man:
        lst.append(i)

if len(lst) != 0:
    for i in lst:
        print(i,end = ' ')
else :
    print('HE GOT AWAY!')
    

