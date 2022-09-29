sen = input()
while sen != '#':
    sen = sen.lower()
    check = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in sen:
        if i in check:
            cnt += 1
    print(cnt)
    sen = input()
