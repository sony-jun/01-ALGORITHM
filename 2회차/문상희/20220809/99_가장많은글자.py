import sys
readsen = sys.stdin.read()

alpha = 'abcdefghijklmnopqrstuvwxyz'
cnt = dict()

for i in readsen:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
max = 0
out = []
for i in alpha:
    if i in cnt:
        if cnt[i] > max:
            out = []
            max = cnt[i]
            out.append(i)
        elif cnt[i] == max:
            out.append(i)

for i in out:
    print(i, end = '')