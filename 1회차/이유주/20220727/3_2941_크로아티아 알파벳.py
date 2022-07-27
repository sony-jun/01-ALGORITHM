alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()

for i in alphabet:
    print(len(n.replace(i, '*')))