alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()

for i in alphabet:
    n = n.replace(i, '*')
print(len(n))