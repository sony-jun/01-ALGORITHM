
while True:
    vowel = ['a', 'e', 'i', 'o', 'u']
    stns = input().lower()
    cnt = 0
    if stns == '#':
        break
    for s in stns:
        if s in vowel:
            cnt += 1
    print(cnt)
