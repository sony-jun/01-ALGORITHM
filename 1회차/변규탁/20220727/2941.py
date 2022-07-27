
list_ = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for char in list_ :
    word = word.replace(char, "*")

print(len(word))