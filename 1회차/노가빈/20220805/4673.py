tlist = list(range(10000))
for i in range(10000):
    try:
        if i < 10:
            num = i + i
            tlist.remove(num)
        elif i < 100:
            num = int(str(i)[0]) +int(str(i)[1]) + i
            tlist.remove(num)
        elif i < 1000:
            num = int(str(i)[0]) +int(str(i)[1])+int(str(i)[2]) + i
            tlist.remove(num)
        else:
            num = int(str(i)[0]) +int(str(i)[1])+int(str(i)[2])+int(str(i)[3]) + i
            tlist.remove(num)

    except ValueError:
        pass
print(tlist)