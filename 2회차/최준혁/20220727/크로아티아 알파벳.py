S = input()
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(cro_list)):
    if cro_list[i] in S:
        S = S.replace(cro_list[i], "*")

print(len(S))

