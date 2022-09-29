word = input()

trans = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

result = 0
for i in word:
    for k in trans:
        if i in k:
            result += trans.index(k) + 3
print(result)
