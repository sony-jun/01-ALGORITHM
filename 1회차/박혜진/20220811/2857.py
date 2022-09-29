fbi_num = []

for i in range(5) :
    fbi = input()

    if 'FBI' in fbi :
        fbi_num.append(i+1)

if fbi_num == [] :
    print('HE GOT AWAY!')

else :
    print(*fbi_num)

