
vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    string = input()
    c = 0
    
    if string == '#':
        break

    for i in string:
        for j in vowel:
            if i == j:
                c += 1
    
    print(c)