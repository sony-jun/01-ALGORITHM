n = input()
dict = {'c=': 1, 'c-': 1, 'dz=': 1, 'd-': 1, 'lj': 1, 'nj': 1, 's=': 1, 'z=': 1}
cnt = 0
cnt += len(n)
res = ''
res += n
for i in dict.keys():
    while i in res:
        res = res.replace(i, " ", 1)
        if len(i) == 2:
            cnt -= 1
        if len(i) == 3:
            cnt -= 2
print(cnt)