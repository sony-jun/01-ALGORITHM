check = []
for i in range(1, 6):
    sen = input()
    if 'FBI' in sen:
        check.append(i)

if check:
    print(*check)
else:
    print('HE GOT AWAY!')