n = input()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0

for i in arr:
    cnt += n.count(i)
    n = n.replace(i, ' ')

cnt += len(n.replace(' ', ''))

print(cnt)
