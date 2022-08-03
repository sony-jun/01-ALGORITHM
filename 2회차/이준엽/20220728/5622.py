word = input()
long =0
if 'OPERATORS' in word :
    long+=11
    word = word.replace('OPERATORS','')
for i in word:
    if i in 'ABC':
        long+=3
    elif i in 'DEF':
        long+=4
    elif i in 'GHI':
        long+=5
    elif i in 'JKL':
        long+=6
    elif i in 'MNO':
        long+=7
    elif i in "PQRS":
        long+=8
    elif i in 'TUV':
        long+=9
    elif i in 'WXYZ':
        long+=10
print(long)