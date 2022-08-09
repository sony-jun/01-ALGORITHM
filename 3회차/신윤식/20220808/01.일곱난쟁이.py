lst = []
lst2 = []
for _ in range(9):
    lst.append(int(input()))

for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            for l in range(k+1, 6):
                for m in range(l+1, 7):
                    for n in range(m+1, 8):
                        for o in range(n+1, 9):
                            if lst[i] + lst[j] + lst[k] + lst[l] + lst[m] + lst[n] + lst[o] == 100:
                                lst2.append(lst[i])
                                lst2.append(lst[j])
                                lst2.append(lst[k])
                                lst2.append(lst[l])
                                lst2.append(lst[m])
                                lst2.append(lst[n])
                                lst2.append(lst[o])
                                break
lst2 = lst2[:7]
lst2.sort()

for p in lst2:
    print(p)