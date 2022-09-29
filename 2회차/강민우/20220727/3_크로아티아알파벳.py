N =input()
cro_word = ['c=' , 'c-' , 'dz=' , 'd-' , 'lj' , 'nj' , 's=' , 'z=' ]

for a in cro_word :
    N = N.replace(a , '@')
print(len(N))
