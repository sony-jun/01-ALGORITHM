
# dwfs = [int(input()) for _ in range(9)]
dwfs = [20, 7, 23, 19, 10, 15, 25, 8, 13]

total = sum(dwfs)

for i in range(9):
    for j in range(i + 1, 9):
        if total - (dwfs[i] + dwfs[j]) == 100:
            ndwf1, ndwr2 = dwfs[i], dwfs[j]

            dwfs.remove(ndwf1)
            dwfs.remove(ndwr2)
            dwfs.sort()

            for d in dwfs:
                print(d)
            break

    if len(dwfs) < 9:
        break
