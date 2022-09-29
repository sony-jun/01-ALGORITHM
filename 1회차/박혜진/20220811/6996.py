for _ in range(int(input())) :
    word1, word2 = input().split()

    ana = []
    for i in word1 :
        ana.append(i)

    for j in word2 :
        if j in ana :
            ana.remove(j)

    if ana == [] :
        print(f'{word1} & {word2} are anagrams.')
        
    else :
        print(f'{word1} & {word2} are NOT anagrams.')
