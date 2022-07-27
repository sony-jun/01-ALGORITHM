cro = ['c=', 'c-', 'dz=', 'lj', 'nj', 's=', 'z=']
word = input()

for i in cro :
    word = word.replace(i, '1')
print(len(word))