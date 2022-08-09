while True:
    T = input()
    S = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    cnt = 0
    for i in T:
        for j in S:
            if i == j:
                cnt += 1
    if i == '#':
        break
    print(cnt)