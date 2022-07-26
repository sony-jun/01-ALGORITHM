num = input()

for i in range(int(num)) :
    vs = i
    for j in str(i) :
        vs += int(j)

    if vs == int(num) :
        print(i)
        break

    if i == int(num)-1 :
        print(0)
        break